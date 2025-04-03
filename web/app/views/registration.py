from ..forms.registration_form import RegistrationForm, ImageForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from ..models import AlumniVerificationRequest
from django.utils.translation import activate
from django.urls import reverse

@csrf_exempt
def registration(request):
    activate('en')  # фиксируем английский язык, чтобы ошибки были на английском

    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if user_form.is_valid() and image_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            # логиним пользователя
            auth_login(request, user)

            # сохраняем изображение, если есть
            if request.FILES:
                profile = image_form.save(commit=False)
                profile.user = user
                profile.save()

            # создаём запрос на верификацию выпускника
            AlumniVerificationRequest.objects.create(user=user)

            # редирект на домашнюю страницу
            return redirect(reverse('home'))  # ← обратите внимание, нужен path name='home'

        # здесь можно логировать ошибки
        print(user_form.errors, image_form.errors)

    else:
        user_form = RegistrationForm()
        image_form = ImageForm()

    return render(request, 'app/register.html', {
        "form": user_form,             # ← важно! шаблон должен получать 'form' для assertFormError
        "image_form": image_form
    })