import pytest
from datetime import date
from django.test import TestCase
from mixer.backend.django import mixer

from fpdc.releases.models import Release

pytestmark = pytest.mark.django_db


class ReleaseTests(TestCase):
    def test_create(self):
        """Ensure we can create an instance of Release."""
        mixer.blend(Release)
        assert Release.objects.count() == 1

    def test_query(self):
        """Ensure we can query for instances."""
        mixer.blend(Release, short="fedora")
        r = Release.objects.get(short__exact="fedora")
        assert r.short == "fedora"

    def test_calculated_fields(self):
        """Ensure we can query calculated fields."""
        mixer.blend(Release, eol_date=date(2018, 5, 29), release_date=date(2017, 7, 11))
        r = Release.objects.get(status__exact="eol")
        assert r.status == "eol"
        assert r.active is False
