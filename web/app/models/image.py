from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to="images/", blank=True, null=True)
