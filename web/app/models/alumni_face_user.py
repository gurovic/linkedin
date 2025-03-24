from django.contrib.auth.models import User
from .alumni_face import AlumniFace
from django.db import models


class AlumniFaceUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.OneToOneField(AlumniFace, on_delete=models.CASCADE)
