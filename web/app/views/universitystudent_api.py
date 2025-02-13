import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import UniversityStudent
from app.serializers.universitystudent_serializer import (
    UniversityStudentSerializer,
)


class UniversityStudentView(APIView):
    def get(self, request):
        university_students = UniversityStudent.objects.all()
        serializer = UniversityStudentSerializer(
            university_students,
            many=True,
        )
        return Response(serializer.data)


class CurrentUniversityStudentView(APIView):
    def get(self, request):
        university_students = UniversityStudent.objects.filter(
            end_year__gte=datetime.datetime.now().year,
        )  | UniversityStudent.objects.filter(
            end_year__isnull=True,
        )
        serializer = UniversityStudentSerializer(
            university_students,
            many=True,
        )
        return Response(serializer.data)
