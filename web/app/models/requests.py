import datetime
from django.db import models
from user import User
from rights import Right

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    right_asked = models.ForeignKey(Right, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    desc = models.TextField()