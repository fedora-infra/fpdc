from datetime import date

import pytest
from django.test import TestCase
from freezegun import freeze_time
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

    @freeze_time("2018-06-01")
    def test_calculated_fields_is_eol(self):
        """Ensure we can query calculated fields."""
        mixer.blend(Release, eol_date=date(2018, 5, 29), release_date=date(2017, 7, 11))
        r = Release.objects.get(status__exact="eol")
        assert r.status == "eol"
        assert r.active is False

    @freeze_time("2018-05-01")
    def test_calculated_fields_is_ga(self):
        """Ensure we can query calculated fields."""
        mixer.blend(Release, eol_date=date(2018, 5, 29), release_date=date(2017, 7, 11))
        r = Release.objects.get(status__exact="ga")
        assert r.status == "ga"
        assert r.active is True

    @freeze_time("2017-06-01")
    def test_calculated_fields_is_development(self):
        """Ensure we can query calculated fields."""
        mixer.blend(Release, eol_date=date(2018, 5, 29), release_date=date(2017, 7, 11))
        r = Release.objects.get(status__exact="development")
        assert r.status == "development"
        assert r.active is False
