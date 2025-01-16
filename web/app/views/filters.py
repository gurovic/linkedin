from django.shortcuts import render
from ..models import UserSkill, Skill
from ..forms import SkillFilterForm
from django.contrib.auth.models import User

def search_by_skills(request):
    form = SkillFilterForm(request.GET or None)
    users = None
    user_objects=None
    if form.is_valid():
        selected_skills = form.cleaned_data['skills']
        if selected_skills:
            # Filter users who have all selected skills
            users = UserSkill.objects.filter(tag__in=selected_skills).values('user').distinct()
            user_ids = users.values_list('user', flat=True)

            user_objects = User.objects.filter(id__in=user_ids)
            context = {
                'form': form,
                'users': user_objects,
            }
    return render(request, 'app/search_by_skills.html', {
        'form': form,
        'userskills': user_objects
    })