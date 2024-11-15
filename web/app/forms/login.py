from django import forms
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    form = None
    if request.method == "POST" :
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, user)
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})