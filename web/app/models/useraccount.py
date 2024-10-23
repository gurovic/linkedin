from django.db import models

class UserAccount(models.Model):
    first_name = models.CharField(max_length=30, default='Иван')
    last_name = models.CharField(max_length=30, default='Иванов')
    patronymic = models.CharField(max_length=30, blank=True)
    school = models.CharField(max_length=100, default="Летово")
    institute = models.CharField(max_length=100, blank=True)
    workplace = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"