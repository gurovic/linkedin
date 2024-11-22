from django.db import models

class Alumni(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    university = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
