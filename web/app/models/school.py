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
        ('LAW', 'Law'),
        ('ART', 'Arts'),
        ('BIO', 'Biology'),
        ('PHY', 'Physics'),
        ('CHEM', 'Chemistry'),
    ]

    subject = models.CharField(max_length=4, choices=MAJOR_CHOICES)

    def __str__(self):
        return self.get_subject_display()


class School(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    majors = models.ManyToManyField(MajorSubject, related_name='schools')

    def __str__(self):
        return self.name