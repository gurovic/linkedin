import datetime
from django.db import models

class AlumniVerificationRequest(models.Model):
    ANSWER_CHOICES = [
        ('NA', 'Not answered'),
        ('AC', 'Accepted'),
        ('DE', 'Declined')
    ]
    surname = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(null=True, blank=True)
    university = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    photo = models.ImageField(upload_to="verif/", blank=True)
    approved = models.CharField(max_length=120, choices=ANSWER_CHOICES, default='NA')
    confirmation_sent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.surname} {self.first_name}, {self.get_approved_display()}'
