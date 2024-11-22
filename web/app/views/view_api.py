from rest_framework import generics
from app.models.alumni import Alumni
from ..serializers.AlumniSerializer import AlumniSerializer

class AlumniListView(generics.ListAPIView):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer
