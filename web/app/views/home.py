from django.shortcuts import render
from django.contrib.auth.models import User
from ..models import Event
from ..models.company import Company

def home(request):
    users = User.objects.all()

    event_objects = Event.objects.all()
    events = [event for event in event_objects if ((not event.already_passed()) and event.allowed)]

    companies = Company.objects.all()

    for event in events:
        if event.picture:
            event.format_image_to_height(300)
            event.save()

    context = {
        'users': users,
        'event_list': events,
        'companies': companies
    }

    return render(request, 'app/home.html', context)