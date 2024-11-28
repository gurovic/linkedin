from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class UnauthorisedAlumni(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=20)  # then it will be replaced with ForeignKey()
    graduation_year = models.IntegerField(validators=[
            MaxValueValidator(2108),
            MinValueValidator(2021)
        ])

    def __str__(self):
        return self.user.username
