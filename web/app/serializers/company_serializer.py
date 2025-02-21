from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from app.models.company import Company


class CompanySerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
