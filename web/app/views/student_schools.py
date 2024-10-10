from django.shortcuts import render, get_object_or_404
from ..models import StudentSchool, School

def student_schools(request, user_id):
    student_schools_list = StudentSchool.objects.filter(student=user_id).order_by('start_year')
    context =  {'student_schools': student_schools_list, 'username': request.user.username}
    return render(request, 'app/student_schools.html', context)
