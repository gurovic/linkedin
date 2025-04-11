from django.contrib.auth.models import User
from django.db import models


class AlumniFace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to="alumni_faces/")

    def __str__(self):
        return f"{self.user.username} - {self.image_path}"

