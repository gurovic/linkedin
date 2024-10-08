from django.db import models
from .topic import Topic
from .employer import Employer

class Vacancy(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    text = models.TextField()
    salary_per_month = models.IntegerField()
    topics = models.ManyToManyField(Topic)