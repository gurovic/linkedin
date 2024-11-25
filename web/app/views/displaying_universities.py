from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from ..models import University, UniversityStudent


def student_universities(request, student):
    student = User.objects.get(id=student)
    universities = University.objects.filter(university_students__student=student)
    student_universities = UniversityStudent.objects.filter(student=student)

    return render(request, 'app/displaying_universities.html', {
        'student': student,
        'universities': universities,
        'universitystudent': student_universities,
    })
