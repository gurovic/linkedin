from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..models import Event
from ..serializers.event_serializer import EventSerializer

class EventListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        events = Event.objects.filter(allowed=True)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
