from rest_framework.views import APIView
from ..models import AlumniVerificationRequest
from ..serializers.verification_serializer import VerificationRequestSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class VerificationDescriptionView(APIView):
    def get(self, request, request_id):
        verification = get_object_or_404(AlumniVerificationRequest, id=request_id)
        serializer = VerificationRequestSerializer(verification)
        return Response(serializer.data)
