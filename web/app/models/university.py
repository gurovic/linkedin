from django.db import models
from multiselectfield import MultiSelectField
from django import forms
from django.contrib.auth.models import User


class University(models.Model):
    COUNTRY_CHOICES = [
        ('RU', 'Russian Federation'),
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('GB', 'United Kingdom'),
        ('DE', 'Germany'),
        ('FR', 'France'),
        ('JP', 'Japan'),
        ('CN', 'China'),
        ('IN', 'India'),
        ('BR', 'Brazil'),
    ]
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
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, default='Smth', choices=COUNTRY_CHOICES)
    majors_availible = MultiSelectField(max_length=100, default='Smth', choices=MAJOR_CHOICES)

    def __str__(self):
        return self.name
