from django.shortcuts import render
from ..models import Event


def event_list_old(request):
    event_objects = Event.objects.all()
    events = [event for event in event_objects if not event.already_passed()]

    for event in events:
        if event.picture:
            event.format_image_to_height(300)
            event.save()

    context = {
        'event_list': events
    }
    return render(request, 'app/event_list.html', context)