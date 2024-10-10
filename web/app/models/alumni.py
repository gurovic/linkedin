from django.contrib.auth.models import User
from django.db import models


class Friend(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')

    def __str__(self):
        # return f"{self.user1}{self.user2}"
        return "User1: Login - User2: Login"
