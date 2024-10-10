from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class User(get_user_model()):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)