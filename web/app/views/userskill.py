
from django.core.exceptions import ValidationError
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import SkillEndorsement, UserSkill
from app.serializers.userskill_serializer import UserSkillSerializer


class UserSkillView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, user_id):
        user_skills = UserSkill.objects.filter(user_id=user_id)
        serializer = UserSkillSerializer(user_skills, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        serializer = UserSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class UserSkillDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, user_id, skill_id):
        try:
            user_skills = UserSkill.objects.filter(user_id=user_id, skill_id=skill_id)
            user_skills.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserSkill.DoesNotExist:
            return Response(
                {"error": "UserSkill not found."},
                status=status.HTTP_404_NOT_FOUND,
            )


class SkillEndorsementView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id, skill_id):
        try:
            user_skill = UserSkill.objects.get(user_id=user_id, id=skill_id)
            endorsements = SkillEndorsement.objects.filter(userskill=user_skill)
            endorsement_data = [
                {"endorser": e.endorser.username}
                for e in endorsements
            ]

            return Response(endorsement_data, status=status.HTTP_200_OK)
        except UserSkill.DoesNotExist:
            return Response(
                {"error": "User or skill not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, user_id, skill_id):
        try:
            endorser = request.user
            user_skill = UserSkill.objects.get(user_id=user_id, id=skill_id)

            endorsement = SkillEndorsement(endorser=endorser, userskill=user_skill)
            endorsement.clean()
            endorsement.save()

            return Response(
                {"message": "Skill endorsement created successfully."},
                status=status.HTTP_201_CREATED,
            )
        except UserSkill.DoesNotExist:
            return Response(
                {"error": "User or skill not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ValidationError as e:
            return Response(
                {"error": e.message},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, user_id, skill_id):
        try:
            endorser = request.user
            user_skill = UserSkill.objects.get(user_id=user_id, id=skill_id)

            endorsement = SkillEndorsement.objects.get(
                endorser=endorser, userskill=user_skill
            )
            endorsement.delete()

            return Response(
                {"message": "Skill endorsement deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except SkillEndorsement.DoesNotExist:
            return Response(
                {"error": "Endorsement not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ValidationError as e:
            return Response(
                {"error": e.message},
                status=status.HTTP_400_BAD_REQUEST,
            )
