# models.py
from django.db import models
from django.contrib.auth.models import User

class JobExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name} ({self.start_year} - {self.end_year})"
