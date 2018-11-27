import datetime
from django.contrib.auth.models import User, Group, ContentType

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from fpdc.releases.models import Release

DATA = {
    "release_id": "fedora-27",
    "short": "fedora",
    "name": "Fedora",
    "version": 27,
    "release_date": "2017-11-14",
    "eol_date": "2018-11-30",
    "sigkey": "0xdeadbeef",
}


class ReleaseViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = mixer.blend(User)
        releases = ContentType.objects.get(app_label="releases")
        releases_permissions = list(releases.permission_set.all())
        group = Group.objects.create(name="releng-team")
        group.permissions.set(releases_permissions)
        group.user_set.add(cls.user)

    def test_create_release(self):
        url = reverse("v1:release-list")
        self.client.force_authenticate(self.__class__.user)
        response = self.client.post(url, DATA, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Release.objects.count() == 1
        assert Release.objects.get().release_id == "fedora-27"

    def test_update_release(self):
        release = mixer.blend(Release)
        url = reverse("v1:release-detail", kwargs={"pk": release.pk})
        self.client.force_authenticate(self.__class__.user)
        response = self.client.put(url, DATA, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert Release.objects.count() == 1
        assert Release.objects.get().release_id == "fedora-27"

    def test_partial_update_release(self):
        release = mixer.blend(Release)
        url = reverse("v1:release-detail", kwargs={"pk": release.pk})
        data = {"release_id": "fedora-28"}
        self.client.force_authenticate(self.__class__.user)
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert Release.objects.count() == 1
        assert Release.objects.get().release_id == "fedora-28"

    def test_delete_release(self):
        release = mixer.blend(Release)
        url = reverse("v1:release-detail", kwargs={"pk": release.pk})
        assert Release.objects.count() == 1
        self.client.force_authenticate(self.__class__.user)
        response = self.client.delete(url, format="json")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Release.objects.count() == 0

    def test_get_release(self):
        release = mixer.blend(Release)
        url = reverse("v1:release-detail", kwargs={"pk": release.pk})
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["release_id"] == release.release_id

    def test_get_release_list(self):
        mixer.cycle(5).blend(Release)
        url = reverse("v1:release-list")
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert Release.objects.count() == 5

    def test_create_release_unauthenticated(self):
        url = reverse("v1:release-list")
        response = self.client.post(url, DATA, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_release_unauthenticated(self):
        release = mixer.blend(Release)
        url = reverse("v1:release-detail", kwargs={"pk": release.pk})
        response = self.client.put(url, DATA, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_partial_update_release_unauthenticated(self):
        release = mixer.blend(Release)
        url = reverse("v1:release-detail", kwargs={"pk": release.pk})
        data = {"release_id": "fedora-28"}
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_release_unauthenticated(self):
        release = mixer.blend(Release)
        url = reverse("v1:release-detail", kwargs={"pk": release.pk})
        assert Release.objects.count() == 1
        response = self.client.delete(url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_active_releases(self):
        active_release = mixer.blend(
            Release,
            release_date=datetime.date.today(),
            eol_date=datetime.date.today() + datetime.timedelta(days=10),
        )
        mixer.blend(
            Release,
            release_date=datetime.date.today(),
            eol_date=datetime.date.today() - datetime.timedelta(days=10),
        )
        url = reverse("v1:release-list")
        response = self.client.get(url, {"active": "true"})
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get("count") == 1
        assert response.json().get("results")[0]["name"] == active_release.name

    def test_get_inactive_releases(self):
        mixer.blend(
            Release,
            release_date=datetime.date.today(),
            eol_date=datetime.date.today() + datetime.timedelta(days=10),
        )
        eol_release = mixer.blend(
            Release,
            release_date=datetime.date.today(),
            eol_date=datetime.date.today() - datetime.timedelta(days=10),
        )
        url = reverse("v1:release-list")
        response = self.client.get(url, {"active": "false"})
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get("count") == 1
        assert response.json().get("results")[0]["name"] == eol_release.name
