from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers.user_serializer import UserDetailSerializer


class UserSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("query", None)
        university = request.GET.get("university", None)
        school = request.GET.get("school", None)
        skills = request.GET.get("skills", None)

        users = User.objects.all()

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

        if university:
            users = users.filter(student__university=university)
        if school:
            users = users.filter(studentschool__school=school)
        if skills:
            for skill in skills.split(","):
                users = users.filter(userskills__skill__name=skill)

        serializer = UserDetailSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
