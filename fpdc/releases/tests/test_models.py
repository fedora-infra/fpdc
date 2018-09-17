import pytest
from mixer.backend.django import mixer


pytestmark = pytest.mark.django_db


class TestReleaseType:
    def test_model(self):
        obj = mixer.blend("releases.ReleaseType")
        assert obj.pk == 1, "Should create a ReleaseType instance"

    def test_model_fields(self):
        obj = mixer.blend(
            "releases.ReleaseType", short="ga", name="Release", suffix="-updates-testing"
        )
        assert obj.short == "ga", "Should have a short field"
        assert obj.name == "Release", "Should have a name field"
        assert obj.suffix == "-updates-testing", "Should have a suffix field"
