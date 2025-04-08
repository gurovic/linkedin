from django.db import models
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError


class University(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
