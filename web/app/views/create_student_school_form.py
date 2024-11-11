from django.shortcuts import redirect, render
from ..forms import StudentSchoolForm
from .view_request import request_view


def create_student_school(request):
    if request.method == "POST":
        form = StudentSchoolForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            user = request.user
            new_form.student = user
            new_form.save()
            return redirect(request_view)
    else:
        form = StudentSchoolForm()

    return render(request, "app/student_school_form.html", {"form": form})