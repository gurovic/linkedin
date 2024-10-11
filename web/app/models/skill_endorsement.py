from django.contrib.auth.models import User
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SkillEndorsement(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='endorsements')
    endorsed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_endorsements')

    class Meta:
        unique_together = ('skill', 'endorsed_by')  # Ограничивает дублирование эндорсментов от одного пользователя

    def __str__(self):
        return f"{self.endorsed_by} endorsed {self.skill}"