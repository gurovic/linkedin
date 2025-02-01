from rest_framework import serializers

from app.models.alumni_verification_request import AlumniVerificationRequest

class AnsVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumniVerificationRequest
        fields = ("approved",)