from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import School, University
from app.serializers.user_serializer import UserDetailSerializer


class UserSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        query = request.data.get("query", None)

        university_name = request.data.get("university", None)
        university = University.objects.filter(name=university_name).first()
        if university is None and university_name not in ["", None]:
            return Response(
                {"error": "Invalid university name."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        school_name = request.data.get("school", None)
        school = School.objects.filter(name=school_name).first()
        if school is None and school_name  not in ["", None]:
            return Response(
                {"error": "Invalid school name."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        skills = request.data.get("skills", [])

        users = User.objects.all().filter(is_superuser=False)

        if query:
            users = (
                users.filter(
                    last_name__icontains=query,
                )
                | users.filter(
                    first_name__icontains=query,
                )
                | users.filter(
                    first_name__icontains=query.split(" ")[0],
                )
                | users.filter(
                    last_name__icontains=query.split(" ")[0],
                )
                | users.filter(
                    first_name__icontains=query.split(" ")[-1],
                )
                | users.filter(
                    last_name__icontains=query.split(" ")[-1],
                )
            )

        if university is not None and university_name not in ["", None]:
            users = users.filter(student__university=university)
        if school is not None and school_name not in ["", None]:
            users = users.filter(studentschool__school=school)
        if skills and len(skills) > 0 and skills[0]:
            for skill in skills:
                users = users.filter(userskills__skill__name=skill)

        serializer = UserDetailSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
