from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_request(request):
    logout(request)
    return redirect('/')