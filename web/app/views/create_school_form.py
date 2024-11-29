from django.shortcuts import redirect, render
from ..forms import SchoolForm
from .index import index


def create_school(request):
    if request.method == "POST":
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = SchoolForm()

    return render(request, "app/school_form.html", {"form": form})