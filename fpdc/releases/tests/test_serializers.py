from django.test import TestCase

from fpdc.releases.serializers import ReleaseTypeSerializer
from mixer.backend.django import mixer


class ReleaseTypeSerializerTests(TestCase):
    def test_serialize(self):
        release_type = mixer.blend("releases.ReleaseType")
        serializer = ReleaseTypeSerializer(release_type)
        assert serializer.data["short"] == release_type.short
        assert serializer.data["name"] == release_type.name
        assert serializer.data["suffix"] == release_type.suffix

    def test_deserialize_invalid(self):
        serializer = ReleaseTypeSerializer(data={"name": None, "short": "short-name"})
        assert serializer.is_valid() is False
