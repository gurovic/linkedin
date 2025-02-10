from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.forms.search_form import UserSearchForm
from app.serializers.user_serializer import UserDetailSerializer


class UserSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        form = UserSearchForm(request.GET or None)
        users = User.objects.all()

        if form.is_valid():
            query = form.cleaned_data.get("query")
            university = form.cleaned_data.get("university")
            school = form.cleaned_data.get("school")

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

        serializer = UserDetailSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
