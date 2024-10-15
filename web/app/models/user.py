from django.contrib.auth import get_user_model
from django.db import models

class User(get_user_model()):
    def __str__(self):
        return self.name