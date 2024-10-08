from django.db import models
from .topic import Topic


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(upload_to="events")
    date = models.DateTimeField()
    participants = models.ManyToManyField("auth.User", related_name="events")
    location = models.CharField(max_length=200)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.name
