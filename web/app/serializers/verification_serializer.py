from rest_framework import serializers
from ..models import AlumniVerificationRequest


class VerificationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumniVerificationRequest
        fields = "__all__"
