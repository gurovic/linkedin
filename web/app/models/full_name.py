from django.db import models


class FullName(models.Model):
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
