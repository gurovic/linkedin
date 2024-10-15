from django.db import models
from django.contrib.auth.models import User

class TypeOfUser(models.Model):
    USER_TYPE_CHOICES = [
        ('AL', 'Alumni'),
        ('ST', 'Student'),
        ('EM', 'Employer')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_of_user = models.CharField(max_length=2, choices=USER_TYPE_CHOICES)