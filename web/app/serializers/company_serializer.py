from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .user_serializer import UserDetailSerializer
from app.models.company import Company


class CompanySerializer(CountryFieldMixin, serializers.ModelSerializer):
    current_workers = UserDetailSerializer(many=True)  
    
    class Meta:
        model = Company
        fields = "__all__"
