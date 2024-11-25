import datetime
from django.db import models
from django.contrib.auth.models import User


class AlumniVerificationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    name = models.CharField(max_length=120)
    photo = models.ImageField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, {self.date}, {self.approved}'
