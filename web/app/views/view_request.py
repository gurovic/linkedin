from django.shortcuts import render
from django.http import Http404
from ..models import Request

def request_view(request):
    try:
        requests_list = Request.objects.filter(answer=None)
    except Request.DoesNotExist:
        raise Http404("Not found any open requests")
    context = {'requests_list': requests_list}
    print(context)
    return render(request, 'app/requests.html', context)
