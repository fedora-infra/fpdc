from django.db import models


# Create your models here.
class ReleaseType(models.Model):
    short = models.CharField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    suffix = models.CharField(max_length=255, blank=True, unique=True)
