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
    country = models.CharField(max_length=100,default='Smth',choices = COUNTRY_CHOICES)
    current_workers = models.ManyToManyField(User, related_name='workers')

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    required_majors = models.ManyToManyField("Major", related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')
    expiration_date = models.DateField(null=True,blank=True)
    required_language = models.ManyToManyField("Language")
    contacts = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return self.name
