from django.contrib.auth.models import User
from rest_framework import serializers

from .serializator import UniversitySerializer
from ..models import UniversityStudent


class UserDetailSerializer(serializers.ModelSerializer):
    university = serializers.SerializerMethodField()
    first_name = User.first_name
    last_name = User.last_name

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'university']

    def get_university(self, obj):
        try:
            university_student = UniversityStudent.objects.filter(student=obj)
            return UniversitySerializer([us.university for us in university_student], many=True).data
        except UniversityStudent.DoesNotExist:
            return None
