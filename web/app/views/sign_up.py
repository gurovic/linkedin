from ..forms.registration_form import RegistrationForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect

@csrf_exempt
def sign_up(request):
    if request.method == "POST" :
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/university')
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})
