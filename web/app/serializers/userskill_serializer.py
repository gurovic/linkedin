from rest_framework import serializers

from app.models import UserSkill


class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = ["id", "skill"]

