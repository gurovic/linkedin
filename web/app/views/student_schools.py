from django.shortcuts import render
from ..models import School

def student_schools(request):
    student_schools_list = School.objects.all().order_by('country')
    context = {'student_schools': student_schools_list, 'username': request.user.username}
    return render(request, 'app/student_schools.html', context)
