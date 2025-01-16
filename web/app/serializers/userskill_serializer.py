from rest_framework import serializers

from app.models import Userskill


class UserskillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userskill
        fields = ["id", "skill"]

