from ..forms.registration_form import RegistrationForm, ImageForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from ..models import AlumniVerificationRequest

@csrf_exempt
def registration(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if user_form.is_valid() and image_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            auth_login(request, user)

            if request.FILES:
                profile = image_form.save(commit=False)
                profile.user = request.user
                profile.save()

            # Create an AlumniVerificationRequest for the new user
            AlumniVerificationRequest.objects.create(user=user)

            return redirect('/')
        print(user_form.errors, image_form.errors)
    else:
        user_form = RegistrationForm()
        image_form = ImageForm()
    return render(request, 'app/register.html', {"user_form": user_form, "image_form": image_form})
