from django.shortcuts import render, get_object_or_404, redirect
from ..models import UniversityStudent
from ..forms.university_forms import UniversityStudentForm
from django.contrib.auth.decorators import login_required
@login_required
def edit_university_student(request, pk):
    # Get the UniversityStudent record, ensuring the logged-in user is the owner
    university_student = get_object_or_404(UniversityStudent, pk=pk)

    if request.method == 'POST':
        form = UniversityStudentForm(request.POST, instance=university_student)
        if form.is_valid():
            form.save()
            return redirect('student_universities')  # Redirect to list view or success page
    else:
        form = UniversityStudentForm(instance=university_student)

    return render(request, 'app/university_student_form.html', {
        'form': form,
        'university_student': university_student,
    })