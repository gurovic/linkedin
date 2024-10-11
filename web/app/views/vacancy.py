import django  # from django.shortcuts import render

from ..models import Event


def render_vacancy(request):
    vacancy_list = Event.objects.all()
    context = {
        'event_list': vacancy_list
    }
    return django.shortcuts.render(request, 'event_list.html', context)