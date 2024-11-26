from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class AuthView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Django creates the session and sets the sessionid
            return JsonResponse({"message": "Login successful"}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=401)
