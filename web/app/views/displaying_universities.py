from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from ..models import University, UniversityStudent


def student_universities(request, student_id):
    student = User.objects.get(id=student_id)
    universities = University.objects.filter(university_students__student_id=student)
    student_universities = UniversityStudent.objects.filter(student_id=student)

    return render(request, 'app/displaying_universities.html', {
        'student': student,
        'universities': universities,
        'universitystudent': student_universities,
    })
