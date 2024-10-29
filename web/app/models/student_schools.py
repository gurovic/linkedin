from django.db import models
from django.contrib.auth.models import User
import datetime
from .school import *

class StudentSchool(models.Model):
    OPTIONS_FOR_LEAVING = [
        ('GR', 'Graduated'),
        ('EX', 'Expelled'),
        ('LE', 'Left'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    start_year = models.DateField(default=datetime.date.today)
    finish_year = models.DateField(default=datetime.date.today, null=True, blank=True)
    why_left = models.CharField(max_length=128, choices=OPTIONS_FOR_LEAVING, blank=True, null=True)

    def __str__(self):
        return f'{str(self.student)} at school {str(self.school)}'