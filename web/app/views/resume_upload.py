from django.shortcuts import render

def upload_form(request):
    return render(request, 'app/upload_test.html')