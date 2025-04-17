from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


from ..models import AlumniVerificationRequest
from ..serializers.verification_serializer import VerificationRequestSerializer

class VerificationDescriptionView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, request_id):
        verification = get_object_or_404(AlumniVerificationRequest, id=request_id)
        serializer = VerificationRequestSerializer(verification)
        return Response(serializer.data)

    def post(self, request):
        surname = request.data.get('surname')
        first_name = request.data.get('firstName')
        middle_name = request.data.get('middleName')
        email = request.data.get('email')
        university = request.data.get('university')
        photo = request.data.get('photo')

        if not (surname and first_name and email and university and photo):
            return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

        AlumniVerificationRequest.objects.create(
            surname=surname,
            first_name=first_name,
            middle_name=middle_name,
            email=email,
            university=university,
            photo=photo
        )

        return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)


    def patch(self, request, request_id):
        verification = get_object_or_404(AlumniVerificationRequest, id=request_id)
        action = request.data.get('action')

        if action == 'approve':
            verification.approved = 'AC'
        elif action == 'decline':
            verification.approved = 'DE'
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

        verification.save()
        return Response({'status': f'{action}d'}, status=status.HTTP_200_OK)
