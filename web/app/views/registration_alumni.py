from ..forms.registration_alumni_form import AlumniForm, RegistrationForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from ..models.unauthorised_alumni import UnauthorisedAlumni


@csrf_exempt
def registration_alumni(request):

    if request.method == "POST":
        post = request.POST
        user_keys = ('csrfmiddlewaretoken', 'username', 'email', 'password1', 'password2')
        alumni_keys = ('university', 'graduation_year')
        user_form = RegistrationForm({k: post[k] for k in user_keys})
        alumni_form = AlumniForm({k: post[k] for k in alumni_keys})
        if user_form.is_valid() and alumni_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            auth_login(request, user)
            data_alumni = alumni_form.cleaned_data
            alumni = UnauthorisedAlumni(user=user, university=data_alumni["university"], graduation_year=data_alumni["graduation_year"])
            alumni.save()
            return redirect('/')
        else:
            print(user_form.errors, alumni_form.errors)
    else:
        user_form = RegistrationForm()
        alumni_form = AlumniForm()
    return render(request, 'app/register_alumni.html', {
        'user_form': user_form,
        'alumni_form': alumni_form
    })
