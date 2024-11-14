from django.shortcuts import render
#from django import forms
from django.contrib.auth.models import User

def home(request):
    users = User.objects.all()
    return render(request, 'app/home.html')


def registration(request):
    return render(request, 'app/register.html', {'users' : users})