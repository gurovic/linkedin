import datetime
from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    RIGHT_CHOICES = [
        ('TW', 'To write posts'),
        ('TC', 'To write comments'),
        ('TE', 'To create events'),
        ('TV', 'To create vacancies'),
        ('TN', 'To change name')
    ]

    ANSWER_CHOICES = [
        ('NA', 'Not answered'),
        ('AC', 'Accepted'),
        ('DE', 'Declined')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    right_asked = models.CharField(max_length=2, choices=RIGHT_CHOICES, default='TC')
    name = models.CharField(max_length=120)
    desc = models.TextField(default='')
    answered = models.CharField(max_length=2, choices=ANSWER_CHOICES, default='NA')


    def __str__(self):
        return f'{self.name}, {self.date}, {self.right_asked}, {self.desc}'