# views.py
from django.shortcuts import render, redirect
from .models import JobExperience
from .forms import JobExperienceForm
from django.contrib.auth.decorators import login_required


@login_required
def job_experience_view(request):
    if request.method == "POST":
        form = JobExperienceForm(request.POST)
        if form.is_valid():
            job_experience = form.save(commit=False)
            job_experience.user = request.user
            job_experience.save()
            return redirect('job_experience')  # перенаправляем на ту же страницу
    else:
        form = JobExperienceForm()

    experiences = JobExperience.objects.filter(user=request.user)
    return render(request, 'job_experience.html', {'form': form, 'experiences': experiences})
