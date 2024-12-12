from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from app.forms.university_forms import UniversityStudentForm
from app.models import UniversityStudent


@login_required
def edit_university_student(request, pk):
    university_student = get_object_or_404(UniversityStudent, pk=pk)

    if request.method == "POST":
        form = UniversityStudentForm(request.POST, instance=university_student)
        if form.is_valid():
            form.save()
            return redirect(
                "student_universities",
                student=university_student.student.id,
            )
    else:
        form = UniversityStudentForm(instance=university_student)

    return render(
        request,
        "app/university_student_form.html",
        {
            "form": form,
            "university_student": university_student,
        },
    )
