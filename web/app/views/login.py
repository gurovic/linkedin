from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Get the username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('/')  # Redirect to home or another page after login
            else:
                # If authentication fails
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form submission.")

    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form': form})
