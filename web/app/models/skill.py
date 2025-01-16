from django.db import models


class skill(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Userskill(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="userskills",
    )
    skill = models.ForeignKey(
        skill,
        on_delete=models.CASCADE,
        related_name="userskills",
    )

    class Meta:
        unique_together = ("user", "skill")

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"
