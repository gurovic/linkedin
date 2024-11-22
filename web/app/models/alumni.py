from django.db import models
from django.contrib.auth.models import User


class Alumni(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField()
    MIN_GRAD_YEAR = 2021
    graduation_year = models.IntegerField()