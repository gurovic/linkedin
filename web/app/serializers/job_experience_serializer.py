from rest_framework import serializers
from ..models import JobExperience

class JobExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobExperience
        fields = ['id', 'company_name', 'start_year', 'end_year', 'position']
        read_only_fields = ['id']