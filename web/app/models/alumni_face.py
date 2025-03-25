from django.contrib.auth.models import User
from django.db import models


class AlumniFace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to="alumni_faces/")
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()

