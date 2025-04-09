from django.db import models
from django.contrib.auth.models import User


class AlumniVerificationRequest(models.Model):
    APPROVAL_CHOICES = [
        ('A', 'Approved'),
        ('R', 'Rejected'),
        ('NA', 'Not Approved Yet'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    university = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='alumni_verification_photos/')
    date = models.DateTimeField(auto_now_add=True)
    approved = models.CharField(max_length=2, choices=APPROVAL_CHOICES, default='NA')

    def __str__(self):
        return f"{self.user.last_name}, {self.get_approved_display()}"