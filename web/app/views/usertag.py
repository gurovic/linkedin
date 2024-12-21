from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import UserTag
from app.serializers.usertag_serializer import UserTagSerializer


class UserTagView(APIView):
    def get(self, request, user_id):
        user_tags = UserTag.objects.filter(user_id=user_id)
        serializer = UserTagSerializer(user_tags, many=True)
        return Response(serializer.data)
