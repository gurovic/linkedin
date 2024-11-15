from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    users = User.objects.all()
    return render(request, 'app/home.html', {'users' : users})