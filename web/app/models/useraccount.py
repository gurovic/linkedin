from django.db import models

class UserAccount(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True)
    school = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    workplace = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"