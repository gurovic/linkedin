from django.shortcuts import redirect, render
from ..forms import AnswerForm
from .view_request import request_view


def create_answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('files')
            return redirect(request_view)
    else:
        form = AnswerForm()

    return render(request, "app/answer_form.html", {"form": form})