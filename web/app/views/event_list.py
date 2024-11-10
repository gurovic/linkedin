from django.shortcuts import render

from ..models import Event


def event_list(request):
    event_list = Event.objects.all()
    context = {
        'event_list': event_list
    }
    return render(request, 'app/event_list.html', context)