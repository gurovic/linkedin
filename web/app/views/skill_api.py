from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Skill
from app.serializers.skill_serializer import SkillSerializer


class SkillView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, skill_id = None):
        if skill_id is None:
            skills = Skill.objects.all()
        else:
            skills = Skill.objects.filter(id=skill_id)
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
