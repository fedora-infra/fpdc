import datetime

import computed_property
from django.db import models


class Release(models.Model):
    release_id = models.CharField(max_length=255, blank=False, unique=True)
    short = models.CharField(max_length=255, blank=False, unique=False)
    version = models.IntegerField(blank=False)
    name = models.CharField(max_length=255, blank=False, unique=False)
    release_date = models.DateField()
    eol_date = models.DateField()
    sigkey = models.CharField(max_length=255, blank=False)
    status = computed_property.ComputedCharField(compute_from="_status", max_length=255, null=True)
    active = computed_property.ComputedBooleanField(compute_from="_active", default=True)

    def _status(self):
        if self.release_date > datetime.date.today():
            return "development"
        if self.eol_date < datetime.date.today():
            return "eol"
        return "ga"

    def _active(self):
        return self.status == "ga"
