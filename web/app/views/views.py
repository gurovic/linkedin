from rest_framework import generics
from app.models.alumni_model import Alumni
from ..serializers.AlumniSerializer import AlumniSerializer

class AlumniListView(generics.ListAPIView):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer
