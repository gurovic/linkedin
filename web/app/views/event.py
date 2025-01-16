from django.core.exceptions import ValidationError
from rest_framework import permissions, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Event
from app.serializers.event_serializer import EventSerializer


class EventView(APIView):
    """POST ALLOWS ONLY multipart/form-data"""

    parser_classes = (MultiPartParser,)

    def get(self, request, event_id=None):
        if not event_id:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
        else:
            events = Event.objects.get(id=event_id)
            serializer = EventSerializer(events)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, event_id):
        event = Event.objects.get(id=event_id)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, event_id):
        Event.objects.get(id=event_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventParticipantsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            participants = event.participants.all()
            participant_data = [
                {"participant": p.username} for p in participants
            ]

            return Response(participant_data, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response(
                {"error": "Event not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, event_id):
        try:
            participant = request.user
            event = Event.objects.get(id=event_id)
            event.participants.add(participant)
            participant_data = [
                {"participant": p.username} for p in event.participants.all()
            ]
            return Response(participant_data, status=status.HTTP_201_CREATED)
        except Event.DoesNotExist:
            return Response(
                {"error": "Event not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ValidationError:
            return Response(
                {"error": "User already a participant."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, event_id):
        try:
            participant = request.user
            Event.objects.get(id=event_id).participants.remove(participant)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response(
                {"error": "Event not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ValidationError:
            return Response(
                {"error": "User not a participant."},
                status=status.HTTP_400_BAD_REQUEST,
            )
