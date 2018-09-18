from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from fpdc.releases.models import ReleaseType


class ReleaseTypeViewTests(APITestCase):
    def test_create_release_type(self):
        url = reverse("v1:releasetype-list")
        data = {"name": "Release", "short": "ga", "suffix": ""}
        response = self.client.post(url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert ReleaseType.objects.count() == 1
        assert ReleaseType.objects.get().name == "Release"

    def test_update_release_type(self):
        release_type = mixer.blend(ReleaseType)
        url = reverse("v1:releasetype-detail", kwargs={"pk": release_type.pk})
        data = {"name": "Release", "short": release_type.short, "suffix": release_type.suffix}
        response = self.client.put(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert ReleaseType.objects.count() == 1
        assert ReleaseType.objects.get().name == "Release"

    def test_partial_update_release_type(self):
        release_type = mixer.blend(ReleaseType)
        url = reverse("v1:releasetype-detail", kwargs={"pk": release_type.pk})
        data = {"name": "Release"}
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert ReleaseType.objects.count() == 1
        assert ReleaseType.objects.get().name == "Release"

    def test_delete_release_type(self):
        release_type = mixer.blend(ReleaseType)
        url = reverse("v1:releasetype-detail", kwargs={"pk": release_type.pk})
        assert ReleaseType.objects.count() == 1
        response = self.client.delete(url, format="json")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert ReleaseType.objects.count() == 0

    def test_get_release_type(self):
        release_type = mixer.blend(ReleaseType)
        url = reverse("v1:releasetype-detail", kwargs={"pk": release_type.pk})
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == release_type.name

    def test_get_release_type_list(self):
        mixer.cycle(5).blend(ReleaseType)
        url = reverse("v1:releasetype-list")
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert ReleaseType.objects.count() == 5
