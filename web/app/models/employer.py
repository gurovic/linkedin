from django.db import models


class Employer(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null="", blank=True)

