from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from ..forms.login_form import EmailLoginForm


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = EmailLoginForm(data=request.POST)
        if form.is_valid():
            # Get the username and password from the form
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = EmailLoginForm()

    return render(request, 'app/login.html', {'form': form})