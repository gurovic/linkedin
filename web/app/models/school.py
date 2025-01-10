from django.db import models
from ..utils import *
from multiselectfield import MultiSelectField

class MajorSubject(models.Model):
    MAJOR_CHOICES = [
        ('CS', 'Computer Science'),
        ('MATH', 'Mathematics'),
        ('ENG', 'English'),
        ('RU', 'Russian Language'),
        ('ART', 'Arts'),
        ('BIO', 'Biology'),
        ('PHY', 'Physics'),
        ('CHEM', 'Chemistry'),
    ]

    subject = models.CharField(max_length=4, choices=MAJOR_CHOICES)

    def __str__(self):
        return self.get_subject_display()


class School(models.Model):
    MAJOR_CHOICES = [
        ('CS', 'Computer Science'),
        ('MATH', 'Mathematics'),
        ('ENG', 'English'),
        ('RU', 'Russian Language'),
        ('ART', 'Arts'),
        ('BIO', 'Biology'),
        ('PHY', 'Physics'),
        ('CHEM', 'Chemistry'),
    ]
    country = models.TextField(max_length=2, choices=COUNTRY_CHOICES)
    name = models.CharField(max_length=40)
    desc = models.TextField(null=True, blank=True)
    majors_available = MultiSelectField(max_length=100, default='Smth', choices=MAJOR_CHOICES)

    def __str__(self):
        return self.name