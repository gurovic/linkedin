from django.db import models

# Create your models here.
class Useracc(models.Model):
    family_name = models.CharField(max_length=200, default='Ivanov')
    name = models.CharField(max_length=200, default='Ivan')
    second_name = models.CharField(max_length=200, default = 'Ivanovich')
    #university = models.CharField(max_length=200)

    description = models.TextField()

    def __str__(self):
        return self.name