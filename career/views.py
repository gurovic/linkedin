from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Experience, Skill

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    experiences = Experience.objects.filter(student=user).order_by('-start_date')
    skills = Skill.objects.filter(user=user)
    return render(request, 'career/profile.html', {
        'user': user,
        'experiences': experiences,
        'skills': skills
    })
