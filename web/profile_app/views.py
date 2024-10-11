from django.shortcuts import render

# Create your views here.
from .models import Useracc

def user_list(request):
    users = Useracc.objects.all()
    return render(request, 'profile_app/user_list.html', {'users': users})