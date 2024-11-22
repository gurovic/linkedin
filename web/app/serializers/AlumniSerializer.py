from rest_framework import serializers
from app.models.alumni import Alumni

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = ['first_name', 'last_name', 'middle_name', 'university']
