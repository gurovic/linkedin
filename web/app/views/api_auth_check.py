from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class AuthCheckView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.user.username == "":
            return JsonResponse({ "error": "Unauthorized!" })
        content = {
            "user": request.user.username
        }
        return JsonResponse(content)