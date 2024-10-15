from ..models import requests
from django.shortcuts import render

def request_view(request):
    requests_list = requests.objects.filter(answered=False)
    context = {'Request': requests_list}
    return render(request, 'linkedin/view_request.html', context)
