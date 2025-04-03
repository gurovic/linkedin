from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..models import Event
from ..serializers.event_serializer import EventSerializer
from django.utils import timezone

class EventListLastAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, _request):
        events = Event.objects.filter(allowed=True).filter(date__gt=timezone.now()).order_by("date")[:5]
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
