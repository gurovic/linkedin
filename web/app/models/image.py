from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_path = models.ImageField(
        upload_to="document_photo/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username}'s profile picture"
