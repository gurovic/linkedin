from django.db import models
from django.contrib.auth.models import User
from .tag import *

class TagUser(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    def __str__(self):
        return f'{str(self.user)} has tag {str(self.tag)}'