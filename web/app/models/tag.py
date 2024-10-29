from django.db import models
from django.contrib.auth.models import User
from .skill_category import SkillCategory

class Tag(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(SkillCategory, on_delete=models.SET_DEFAULT, default=1)
    level = models.IntegerField(choices=[
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert')
    ])
    verified_by = models.ManyToManyField(
        User,
        related_name='verified_skills',
        blank=True
    )

    def __str__(self):
        return self.name

    @property
    def verification_count(self):
        return self.verified_by.count()
