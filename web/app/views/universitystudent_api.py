import datetime

from rest_framework.response import Response
from rest_framework.exceptions import bad_request
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED

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


class UniversityStudentCreateView(APIView):
    def post(self, request):
        serializer = UniversityStudentSerializer(data=request.data)
        if not serializer.is_valid():
            raise bad_request(request, Exception("Invalid university-student relation representation!"))
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    