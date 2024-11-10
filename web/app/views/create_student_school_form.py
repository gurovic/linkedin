from django.shortcuts import redirect, render
from ..forms import StudentSchoolForm
from .view_request import request_view


def create_student_school(request):
    if request.method == "POST":
        form = StudentSchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('files')
            return redirect(request_view)
    else:
        form = StudentSchoolForm()

    return render(request, "app/student_school_form.html", {"form": form})