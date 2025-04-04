from rest_framework import serializers
from app.models.company import Vacancy
from app.models.major import Major
from app.models.language import Language
from app.models.company import Company

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ["id", "name"]

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["id", "name"]

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name"]

class VacancySerializer(serializers.ModelSerializer):
    required_majors = MajorSerializer(many=True, read_only=True)
    required_language = LanguageSerializer(many=True, read_only=True)
    company = CompanySerializer(read_only=True)  
    
    class Meta:
        model = Vacancy
        fields = "__all__"