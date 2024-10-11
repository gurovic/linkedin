from ..models import requests, rights, user
from django.shortcuts import render

def request_view(request):
    requests_list = requests.objects.all()
    context = {'Request': requests_list}
    return render(request, 'linkedin/view_request.html', context)
