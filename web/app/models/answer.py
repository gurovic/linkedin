import datetime
from django.db import models
from .requests import Request

class Answer(models.Model):
    request_answered = models.OneToOneField(Request, on_delete=models.CASCADE)
    date = datetime.datetime.now()
    name = models.CharField(max_length=120)
    desc = models.TextField(default='')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, {self.desc}, {self.approved}, {self.date}'
