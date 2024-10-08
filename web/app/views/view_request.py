from ..models import requests, rights, user
from django.shortcuts import render

def request_view(request, requests_id):
    context = {'Request': requests}
    requests_list = requests.objects.all()
    return render(request, 'linkedin/view_request.html', context)
