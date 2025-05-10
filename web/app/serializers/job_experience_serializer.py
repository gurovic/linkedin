from rest_framework import serializers
from ..models import JobExperience


class JobExperienceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = JobExperience
        fields = ['id', 'user', 'company_name', 'position', 'start_year', 'end_year']