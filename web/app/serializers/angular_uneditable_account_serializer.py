from django.contrib.auth.models import User
from rest_framework import serializers
from .university_serializer import UniversitySerializer
from .universitystudent_serializer import UniversityStudentSerializer
from .school_serializer import SchoolSerializer
from ..models import UniversityStudent, StudentSchool

class AngularUserDetailSerializer(serializers.ModelSerializer):
    university = serializers.SerializerMethodField()
    university_student = serializers.SerializerMethodField()
    first_name = User.first_name
    last_name = User.last_name

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'university', 'university_student']

    def get_university(self, obj):
        university_student = UniversityStudent.objects.filter(student=obj)
        if not university_student:
            return None
        return UniversitySerializer([us.university for us in university_student], many=True).data

    def get_university_student(self, obj):
        university_student = UniversityStudent.objects.filter(student=obj)
        if not university_student:
            return None
        return UniversityStudentSerializer(university_student, many=True).data