from django.shortcuts import render
from ..models import Event


def event_list(request):
    event_objects = Event.objects.all()
    event_list = [event for event in event_objects if not event.already_passed()]

    for event in event_list:
        try:
            event.format_image_to_height(300)
            event.save()
        except ValueError as e:
            print(f"Ошибка форматирования изображения для события {event.name}: {e}")

    context = {
        'event_list': event_list
    }
    return render(request, 'app/event_list.html', context)