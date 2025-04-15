from rest_framework.response import Response
from ..models.university import University
from ..serializers.university_serializer import UniversitySerializer
from rest_framework.views import APIView

class UniversityView(APIView):
    def get(self, request, university_id):
        university = University.objects.get(id=university_id)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)
