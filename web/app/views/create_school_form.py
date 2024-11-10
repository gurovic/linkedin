from django.shortcuts import redirect, render
from ..forms import SchoolForm
from .view_request import request_view


def create_school(request):
    if request.method == "POST":
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request_view)
    else:
        form = SchoolForm()

    return render(request, "app/school_form.html", {"form": form})