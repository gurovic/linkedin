from django.shortcuts import render
#from django import forms

def home(request):
    return render(request, 'app/home.html')

def registration(request):
    return render(request, 'app/register.html')