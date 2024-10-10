from django.db import models
from django.contrib.auth.models import User

from .school import *

class StudentSchool(models.Model):
    OPTIONS_FOR_LEAVING = [
        ('graduated', 'Выпустился'),
        ('expelled', 'Был выгнан'),
        ('left', 'Самостоятельно ушел'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    finish_year = models.IntegerField(null=True, blank=True)
    why_left = models.CharField(max_length=128, choices=OPTIONS_FOR_LEAVING, blank=True, null=True)

    def __str__(self):
        return f'{str(self.student)} at school {str(self.school)}'