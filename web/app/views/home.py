from django.shortcuts import render
from django.contrib.auth.models import User
from ..models.unauthorised_alumni import UnauthorisedAlumni
from ..models.alumni import Alumni


def home(request):
    users = User.objects.all()
    unauthorised_alumnus = UnauthorisedAlumni.objects.all()
    alumnus = Alumni.objects.all()
    return render(request, 'app/home.html',
                  {'users': users, 'unauthorised_alumnus': unauthorised_alumnus, 'alumnus': alumnus})
