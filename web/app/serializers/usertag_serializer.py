from rest_framework import serializers

from app.models import UserTag


class UserTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTag
        fields = "__all__"

