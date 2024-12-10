from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ..models import StudentSchool, UniversityStudent


def account_view(request, user_id):
    user = User.objects.get(id=user_id)
    if user_id != request.user.id:
        student_schools_list = StudentSchool.objects.filter(student=user)
        student_universities_list = UniversityStudent.objects.filter(student=user)
        return render(request, 'app/uneditable_account.html', {
            'user': user,
            'student_schools': student_schools_list,
            'student_universities': student_universities_list,
        })
    else:
        return redirect("index")
