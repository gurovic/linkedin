from django.shortcuts import redirect, render

from ..forms.new_request_form import RequestForm
from .view_request import request_view


def create_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('files')
            return redirect(request_view)
    else:
        form = RequestForm()
    return render(request, "app/request_form.html", {"form": form})