from rest_framework import serializers
from ..models import StudentSchool
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSchool
        fields = "__all__"