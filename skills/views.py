from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Skill, Skill_level
from itertools import groupby
from operator import attrgetter


def user_profile(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)

    user_skills = Skill.objects.filter(student=profile_user).order_by('category', 'name')
    skill_levels = Skill_level.objects.filter(student=profile_user)

    skills_with_levels = {sl.name.id: sl.get_level_display() for sl in skill_levels}

    grouped_skills = {}
    for category, skills in groupby(user_skills, key=attrgetter('category')):
        category_skills = []
        for skill in skills:
            skill_info = {
                'name': skill.name,
                'verified': skill.verified,
                'level': skills_with_levels.get(skill.id, 'Не указан')
            }
            category_skills.append(skill_info)
        grouped_skills[category] = category_skills

    context = {
        'profile_user': profile_user,
        'grouped_skills': grouped_skills,
    }

    return render(request, 'career/profile.html', context)