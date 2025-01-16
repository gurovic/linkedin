from rest_framework import serializers

from app.models import UserSkill


class UserTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = ["id", "tag"]

