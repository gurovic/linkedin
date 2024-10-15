# users/person_profile_models.py
from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
