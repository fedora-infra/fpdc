from django.test import TestCase
from mixer.backend.django import mixer

from fpdc.components.models import RPMPackage, Module, Container


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


class ModulesTest(TestCase):
    def test_create(self):
        """Ensure we can create an instance of Modules."""
        mixer.blend(Module)
        assert Module.objects.count() == 1

    def test_query(self):
        """Ensure we can query for instances."""
        mixer.blend(Module, name="eog")
        r = Module.objects.get(name__exact="eog")
        assert r.name == "eog"

    def test_dist_git_url(self):
        """ Ensure the dist_git_url field is properly computed """
        mixer.blend(Module, name="eog")
        r = Module.objects.get(name__exact="eog")
        assert r.dist_git_url == "https://src.fedoraproject.org/modules/eog"


class ContainerTest(TestCase):
    def test_create(self):
        """Ensure we can create an instance of Modules."""
        mixer.blend(Container)
        assert Container.objects.count() == 1

    def test_query(self):
        """Ensure we can query for instances."""
        mixer.blend(Container, name="origin")
        r = Container.objects.get(name__exact="origin")
        assert r.name == "origin"

    def test_dist_git_url(self):
        """ Ensure the dist_git_url field is properly computed """
        mixer.blend(Container, name="origin")
        r = Container.objects.get(name__exact="origin")
        assert r.dist_git_url == "https://src.fedoraproject.org/container/origin"
