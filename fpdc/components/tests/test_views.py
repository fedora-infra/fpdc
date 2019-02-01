from django.contrib.auth.models import User, Group, ContentType

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from fpdc.components.models import RPMPackage

DATA = {"name": "firefox", "point_of_contact": "gecko-maint"}


class RPMPackageViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = mixer.blend(User)
        components = ContentType.objects.get(app_label="components")
        components_permissions = list(components.permission_set.all())
        group = Group.objects.create(name="releng-team")
        group.permissions.set(components_permissions)
        group.user_set.add(cls.user)

    def test_create_rpm(self):
        url = reverse("v1:rpmpackage-list")
        self.client.force_authenticate(self.__class__.user)
        response = self.client.post(url, DATA, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert RPMPackage.objects.count() == 1
        assert RPMPackage.objects.get().name == "firefox"

    def test_update_rpm(self):
        rpm = mixer.blend(RPMPackage)
        url = reverse("v1:rpmpackage-detail", kwargs={"pk": rpm.pk})
        self.client.force_authenticate(self.__class__.user)
        response = self.client.put(url, DATA, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert RPMPackage.objects.count() == 1
        assert RPMPackage.objects.get().name == "firefox"

    def test_partial_update_rpm(self):
        rpm = mixer.blend(RPMPackage)
        url = reverse("v1:rpmpackage-detail", kwargs={"pk": rpm.pk})
        data = {"name": "guake"}
        self.client.force_authenticate(self.__class__.user)
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert RPMPackage.objects.count() == 1
        assert RPMPackage.objects.get().name == "guake"

    def test_delete_rpm(self):
        rpm = mixer.blend(RPMPackage)
        url = reverse("v1:rpmpackage-detail", kwargs={"pk": rpm.pk})
        assert RPMPackage.objects.count() == 1
        self.client.force_authenticate(self.__class__.user)
        response = self.client.delete(url, format="json")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert RPMPackage.objects.count() == 0

    def test_get_rpm(self):
        rpm = mixer.blend(RPMPackage)
        url = reverse("v1:rpmpackage-detail", kwargs={"pk": rpm.pk})
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == rpm.name

    def test_get_rpm_list(self):
        mixer.cycle(5).blend(RPMPackage)
        url = reverse("v1:rpmpackage-list")
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert RPMPackage.objects.count() == 5

    def test_create_rpm_unauthenticated(self):
        url = reverse("v1:rpmpackage-list")
        response = self.client.post(url, DATA, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_rpm_unauthenticated(self):
        rpm = mixer.blend(RPMPackage)
        url = reverse("v1:rpmpackage-detail", kwargs={"pk": rpm.pk})
        response = self.client.put(url, DATA, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_partial_update_rpm_unauthenticated(self):
        rpm = mixer.blend(RPMPackage)
        url = reverse("v1:rpmpackage-detail", kwargs={"pk": rpm.pk})
        data = {"name": "guake"}
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_rpm_unauthenticated(self):
        rpm = mixer.blend(RPMPackage)
        url = reverse("v1:rpmpackage-detail", kwargs={"pk": rpm.pk})
        assert RPMPackage.objects.count() == 1
        response = self.client.delete(url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
