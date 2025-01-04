from django.contrib.auth.models import User
from rest_framework import serializers

from .university_serializer import UniversitySerializer
from .school_serializer import SchoolSerializer
from ..models import UniversityStudent, StudentSchool


class UserDetailSerializer(serializers.ModelSerializer):
    university = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField()
    first_name = User.first_name
    last_name = User.last_name

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'university', 'school']

    def get_university(self, obj):
        try:
            university_student = UniversityStudent.objects.filter(student=obj)
            return UniversitySerializer([us.university for us in university_student], many=True).data
        except UniversityStudent.DoesNotExist:
            return None
    
    def get_school(self, obj):
        try:
            student_school = StudentSchool.objects.filter(student=obj)
            return SchoolSerializer([us.school for us in student_school], many=True).data
        except StudentSchool.DoesNotExist:
            return None