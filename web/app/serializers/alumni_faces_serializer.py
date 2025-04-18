from rest_framework import serializers
from ..models import AlumniFace

class AlumniFaceSerializer(serializers.ModelSerializer):
     class Meta:
         model = AlumniFace
         fields = "id", "image_path"