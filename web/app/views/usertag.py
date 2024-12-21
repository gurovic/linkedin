
from django.core.exceptions import ValidationError
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import SkillEndorsement, UserTag
from app.serializers.usertag_serializer import UserTagSerializer


class UserTagView(APIView):
    def get(self, request, user_id):
        user_tags = UserTag.objects.filter(user_id=user_id)
        serializer = UserTagSerializer(user_tags, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        serializer = UserTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class SkillEndorsementView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id, skill_id):
        try:
            user_tag = UserTag.objects.get(user_id=user_id, id=skill_id)
            endorsements = SkillEndorsement.objects.filter(usertag=user_tag)
            endorsement_data = [
                {"endorser": e.endorser.username}
                for e in endorsements
            ]

            return Response(endorsement_data, status=status.HTTP_200_OK)
        except UserTag.DoesNotExist:
            return Response(
                {"error": "User or skill not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, user_id, skill_id):
        try:
            endorser = request.user
            user_tag = UserTag.objects.get(user_id=user_id, id=skill_id)

            endorsement = SkillEndorsement(endorser=endorser, usertag=user_tag)
            endorsement.clean()
            endorsement.save()

            return Response(
                {"message": "Skill endorsement created successfully."},
                status=status.HTTP_201_CREATED,
            )
        except UserTag.DoesNotExist:
            return Response(
                {"error": "User or skill not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ValidationError as e:
            return Response(
                {"error": e.message},
                status=status.HTTP_400_BAD_REQUEST,
            )
