from rest_framework import serializers

from app.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "name", "description", "picture", "date", "location")
