from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class AuthCheckView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.user.username == "":
            return Response({ "error": "Unauthorized!" }, status=401)
        content = {
            "user": request.user.username
        }
        return Response(content)