from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from ..models import AlumniVerificationRequest
from ..serializers.verification_serializer import VerificationRequestSerializer
from django.shortcuts import get_object_or_404


class VerificationDescriptionView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, request_id):
        verification = get_object_or_404(AlumniVerificationRequest, id=request_id)
        serializer = VerificationRequestSerializer(verification)
        return Response(serializer.data)

    def post(self, request):
        serializer = VerificationRequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Форма успешно сохранена"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)