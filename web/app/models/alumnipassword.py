from django.db import models


class AlumniPassword(models.Model):
    user = models.OneToOneField(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="alumnipassword",
    )
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.user.username} - пароль незарегистрированного"

