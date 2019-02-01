from django.conf import settings
from django.db import models


class RPMPackage(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    point_of_contact = models.CharField(max_length=100, blank=False)

    @property
    def dist_git_url(self):
        return settings.DIST_GIT_URL.format(namespace="rpms", name=self.name)
