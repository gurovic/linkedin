from django.db import models
from .full_name import FullName
from .topic import Topic


class Alumni(models.Model):
    name = models.ForeignKey(FullName, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)