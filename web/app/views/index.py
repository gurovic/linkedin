from django.http import HttpResponse
from django.shortcuts import render

from ..models import *


def index(request, company=None):
    vacancy_list = Vacancy.objects.all()
    context = {
        "vacancy_list": vacancy_list,
        "company": company
    }
    return render(request, "../templates/app/index.html", context)
