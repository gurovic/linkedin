from django.shortcuts import render
from ..models import StudentSchool

def student_schools(request):
    student = request.user
    student_schools_list = StudentSchool.objects.all().filter(student=student)
    context = {'student_schools': student_schools_list, 'username': request.user.username}
    return render(request, 'app/student_schools.html', context)
