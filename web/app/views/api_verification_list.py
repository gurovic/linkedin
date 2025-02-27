from rest_framework.views import APIView
from ..models import AlumniVerificationRequest
from ..serializers.verification_serializer import VerificationRequestSerializer
from rest_framework.response import Response


class VerificationRequestView(APIView):
    def get(self, request):
        verifications = AlumniVerificationRequest.objects.filter(approved="NA")
        serializer = VerificationRequestSerializer(verifications, many=True)
        return Response(serializer.data)
