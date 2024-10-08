from django.db import models

class Right(models.Model):
    RIGHT_CHOICES = [
        ('TW', 'To write posts'),
        ('TC', 'To write comments'),
        ('TE', 'To create events'),
        ('TV', 'To create vacancies'),
        ('TN', 'To change name')
    ]
    right = models.CharField(max_length=2, choices=RIGHT_CHOICES)
