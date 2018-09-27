from django.test import TestCase

from fpdc.releases.serializers import ReleaseSerializer
from mixer.backend.django import mixer


class ReleaseSerializerTests(TestCase):
    def test_serialize(self):
        release = mixer.blend("releases.Release")
        serializer = ReleaseSerializer(release)
        assert serializer.data["short"] == release.short
        assert serializer.data["version"] == release.version

    def test_deserialize_invalid(self):
        serializer = ReleaseSerializer(data={"release_id": None, "short": "short-name"})
        assert serializer.is_valid() is False

    def test_calculated_fields(self):
        release = mixer.blend("releases.Release", eol_date="2017-01-01")
        serializer = ReleaseSerializer(release)
        assert serializer.data["status"] == "eol"
        assert serializer.data["active"] is False
