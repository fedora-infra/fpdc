from django.test import TestCase
from mixer.backend.django import mixer

from fpdc.components.models import RPMPackage


class RPMPackageTest(TestCase):
    def test_create(self):
        """Ensure we can create an instance of RPMPackage."""
        mixer.blend(RPMPackage)
        assert RPMPackage.objects.count() == 1

    def test_query(self):
        """Ensure we can query for instances."""
        mixer.blend(RPMPackage, name="firefox")
        r = RPMPackage.objects.get(name__exact="firefox")
        assert r.name == "firefox"

    def test_dist_git_url(self):
        """ Ensure the dist_git_url field is properly computed """
        mixer.blend(RPMPackage, name="firefox")
        r = RPMPackage.objects.get(name__exact="firefox")
        assert r.dist_git_url == "https://src.fedoraproject.org/rpms/firefox"
