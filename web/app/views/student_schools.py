from django.shortcuts import render
from ..models import StudentSchool

def student_schools(request):
    student_schools_list = StudentSchool.objects.all().order_by('start_year')
    context =  {'student_schools': student_schools_list, 'username': request.user.username}
    return render(request, 'app/student_schools.html', context)
