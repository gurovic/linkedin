from django.shortcuts import render


def index(request):
    context = {'index':0}
    return render(request, "app/index.html", context)
