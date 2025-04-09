from rest_framework import serializers
from ..models import University
class SmallUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "name", "country"