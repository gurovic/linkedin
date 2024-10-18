from django.db import models
from django.contrib.auth.models import User
from django import forms

class Company(models.Model):
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

    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    country = forms.ChoiceField(choices = COUNTRY_CHOICES)
    current_workers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workers')

    def __str__(self):
        return self.name


class Vacancy(models.Model):
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
    description = models.TextField(null=True,blank=True)
    needed_majorsubject=forms.ChoiceField(choices = MAJOR_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')

