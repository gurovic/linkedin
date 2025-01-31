import datetime
from django.db import models
from django.contrib.auth.models import User


class AlumniVerificationRequest(models.Model):
    ANSWER_CHOICES = [
        ('NA', 'Not answered'),
        ('AC', 'Accepted'),
        ('DE', 'Declined')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    photo = models.ImageField(upload_to = "verif/", blank=True)
    approved = models.CharField(max_length=120, choices=ANSWER_CHOICES, default='NA')

    def __str__(self):
        return f'{self.user.last_name}, {self.get_approved_display()}'
