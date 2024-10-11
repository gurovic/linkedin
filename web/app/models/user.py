from django.contrib.auth import get_user_model
from django.db import models
from . import rights

class User(get_user_model()):
    def __str__(self):
        return self.name
    rights = models.ManyToManyField(rights.Right)