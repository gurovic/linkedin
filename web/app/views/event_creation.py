from django.shortcuts import redirect, render

from app.forms.event_creation_form import EventForm


def event_creation(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("event_list_old")
    else:
        form = EventForm()
    return render(request, "app/event_creation.html", {"form": form})
