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
    release_type = computed_property.ComputedCharField(
        compute_from="_release_type", max_length=255, null=True
    )
    active = computed_property.ComputedBooleanField(compute_from="_active", default=True)

    @property
    def _release_type(self):
        if self.release_date > datetime.date.today():
            return "development"
        if self.eol_date < datetime.date.today():
            return "eol"
        return "ga"

    @property
    def _active(self):
        return self.release_type == "ga"
