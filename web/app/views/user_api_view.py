from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserDetailSerializer

@permission_classes([IsAuthenticated])
class UserDetailView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
