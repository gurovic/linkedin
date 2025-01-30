from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models.alumni_verification_request import AlumniVerificationRequest
from .serializers.verification_ans_serializer import AnsVerificationSerializer
from rest_framework.views import APIView


class AnsVerificationView(APIView):
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        req = get_object_or_404(AlumniVerificationRequest, pk=pk)
        app_or_dec = request.data.get('approved')

        if app_or_dec is None:
            return Response({"error": "Invalid or missing 'status' field."}, status=status.HTTP_400_BAD_REQUEST)

        req.approved = app_or_dec
        req.save()
        return Response(AnsVerificationSerializer(req).data, status=status.HTTP_200_OK)
