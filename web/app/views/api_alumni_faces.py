from rest_framework.views import APIView
from ..models import AlumniFace
from ..serializers.alumni_faces_serializer import AlumniFaceSerializer
from rest_framework.response import Response


class AlumniFacesListView(APIView):
    def get(self, _request):
        alumni_faces = AlumniFace.objects.all()
        serializer = AlumniFaceSerializer(alumni_faces, many=True)
        return Response(serializer.data)