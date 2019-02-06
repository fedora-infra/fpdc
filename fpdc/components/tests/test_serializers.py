from django.test import TestCase

from fpdc.components.serializers import RPMPackageSerializer, ModuleSerializer
from mixer.backend.django import mixer


class RPMPackageSerializerTests(TestCase):
    def test_serialize(self):
        rpm = mixer.blend("components.RPMPackage")
        serializer = RPMPackageSerializer(rpm)
        assert serializer.data["name"] == rpm.name
        assert serializer.data["point_of_contact"] == rpm.point_of_contact
        assert serializer.data["dist_git_url"] == rpm.dist_git_url

    def test_deserialize_invalid(self):
        serializer = RPMPackageSerializer(data={"rpmpackage_id": None, "name": "name"})
        assert serializer.is_valid() is False


class ModuleSerializerTests(TestCase):
    def test_serialize(self):
        module = mixer.blend("components.Module")
        serializer = ModuleSerializer(module)
        assert serializer.data["name"] == module.name
        assert serializer.data["point_of_contact"] == module.point_of_contact
        assert serializer.data["dist_git_url"] == module.dist_git_url

    def test_deserialize_invalid(self):
        serializer = ModuleSerializer(data={"module_id": None, "name": "name"})
        assert serializer.is_valid() is False
