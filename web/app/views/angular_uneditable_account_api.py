from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from ..serializers.angular_uneditable_account_serializer import AngularUserDetailSerializer


@api_view(['GET'])
def user_detail_api_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(
            {"detail": "User not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = AngularUserDetailSerializer(user)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def self_detail_api_view(request):
    user = request.user
    serializer = AngularUserDetailSerializer(user)
    return Response(serializer.data)
