from ..forms.registration_form import RegistrationForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login

@csrf_exempt
def registration(request):
    form = None
    if request.method == "POST" :
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})