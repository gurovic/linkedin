from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import University
from ..serializers import UniversitySerializer

@api_view(['GET'])
def university_list(request):
    universities = University.objects.all()
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data)

