from django.shortcuts import redirect, render

from app.forms.event_creation_form import EventForm
from app.views.event_list import event_list


def event_creation(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(event_list)
    else:
        form = EventForm()
    return render(request, "event_creation.html", {"form": form})
