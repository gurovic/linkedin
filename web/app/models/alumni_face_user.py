from django.contrib.auth.models import User
from django.db import models


class AlumniFaceUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_path = models.ImageField(
        upload_to="alumnus_faces_photo/",
    )
