from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=32)