from django.db import models
from django.contrib.auth.models import User
import datetime
from .school import School

class StudentSchool(models.Model):
    OPTIONS_FOR_LEAVING = [
        ('GR', 'Выпустился'),
        ('EX', 'Исключён'),
        ('LE', 'Ушёл по собственному желанию'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    start_year = models.IntegerField(default=datetime.date.today().year)
    finish_year = models.IntegerField(default=datetime.date.today().year, null=True, blank=True)
    why_left = models.CharField(max_length=128, choices=OPTIONS_FOR_LEAVING, blank=True, null=True)

    def __str__(self):
        return f'{str(self.student)} at school {str(self.school)}'