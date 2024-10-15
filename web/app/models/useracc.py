from django.db import models


# Create your models here.
class Useracc(models.Model):
    second_name = models.CharField(max_length=200, default='Ivanov')
    first_name = models.CharField(max_length=200, default='Ivan')
    patronym = models.CharField(max_length=200, default='Ivanovich')
    university = models.CharField(max_length=200, default='No university')

    # description = models.TextField()

    def __str__(self):
        return f"{self.second_name} {self.first_name}"
