from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import StudentSchool, UniversityStudent

# Serializer for the User model to send user details in JSON format
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']

# Serializer for StudentSchool to send school-related data
class StudentSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSchool
        fields = ['school', 'start_year', 'finish_year', 'get_why_left_display']
    
# Serializer for UniversityStudent to send university-related data
class UniversityStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityStudent
        fields = ['university', 'start_date', 'end_date', 'get_leave_reason_display']
