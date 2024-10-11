from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30, default='Без категории')
    description = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Skill_level(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField(choices=[
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert')
    ])