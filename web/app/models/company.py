from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    country = CountryField()
    current_workers = models.ManyToManyField(User, related_name='workers')
    website = models.URLField("company website url")

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
