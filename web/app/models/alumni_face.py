from django.contrib.auth.models import User
from django.db import models


class AlumniFace(models.Model):
    image_path = models.ImageField(
        upload_to="alumnus_faces_photo/",
    )
