from django.db import models
from employer import Employer


class Vacancy(models.Model):
    def __str__(self):
        return f"{self.author}'s vacancy {self.id}"
    author = models.ForeignKey(Employer, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    salary_per_month = models.IntegerField(default=0)