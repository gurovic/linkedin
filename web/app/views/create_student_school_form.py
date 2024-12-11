from django.shortcuts import get_object_or_404, redirect, render

from app.forms import StudentSchoolForm
from app.models import StudentSchool


def create_or_edit_student_school(request, pk=None):
    if pk:
        student_school = get_object_or_404(StudentSchool, pk=pk)
        if student_school.student != request.user:
            return redirect("student_schools")
    else:
        student_school = None

    if request.method == "POST":
        form = StudentSchoolForm(request.POST, instance=student_school)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.student = request.user
            new_form.save()
            return redirect("student_schools")
    else:
        form = StudentSchoolForm(instance=student_school)

    return render(request, "app/student_school_form.html", {"form": form})
