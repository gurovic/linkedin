from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
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
    name = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='RU')

    def __str__(self):
        return self.get_name_display()

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

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    needed_majorsubject=models.ManyToManyField(MajorSubject)
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    vacancies = models.ManyToManyField(Vacancy)
    current_workers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    def __str__(self):
        return self.name


