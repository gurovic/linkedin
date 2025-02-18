from django.contrib.auth.models import User
from rest_framework import serializers
from .university_serializer import UniversitySerializer
from .school_serializer import SchoolSerializer
from ..models import UniversityStudent, StudentSchool

class AngularUserDetailSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()
    university = serializers.SerializerMethodField()
    first_name = User.first_name
    last_name = User.last_name

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'university', 'school']

    def get_university(self, obj):
        university_student = UniversityStudent.objects.filter(student=obj)
        if not university_student:
            return None
        return UniversitySerializer([us.university for us in university_student], many=True).data
    
    def get_school(self, obj):
        student_school = StudentSchool.objects.filter(student=obj)
        if not student_school:
            return None
        return SchoolSerializer([us.school for us in student_school], many=True).data