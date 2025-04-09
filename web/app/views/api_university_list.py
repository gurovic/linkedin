from rest_framework.views import APIView
from ..models import University
from ..serializers.small_university_serializer import SmallUniversitySerializer
from rest_framework.response import Response


class UniversityListView(APIView):
    def get(self, _request):
        universities = University.objects.all()
        serializer = SmallUniversitySerializer(universities, many=True)
        return Response(serializer.data)
