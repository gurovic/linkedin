from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from ..forms import TagForm
from ..models import Tag


@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            messages.success(request, 'Навык успешно добавлен!')
            return redirect('profile', user_id=request.user.id)
    else:
        form = TagForm()

    return render(request, 'app/add_tags.html', {'form': form})

@login_required
def delete_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id, user=request.user)
    tag.delete()
    messages.success(request, 'Навык удален!')
    return redirect('profile', user_id=request.user.id)


@login_required
def verify_skill(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)

    if tag.student == request.user:
        messages.error(request, 'Вы не можете верифицировать собственные навыки')
        return redirect('profile', user_id=tag.student.id)

    if request.user not in tag.verified_by.all():
        tag.verified_by.add(request.user)
        messages.success(request, f'Вы подтвердили навык "{tag.name}"')
    else:
        tag.verified_by.remove(request.user)
        messages.success(request, f'Вы отменили подтверждение навыка "{tag.name}"')

    return redirect('profile', user_id=tag.student.id)

def profile_view(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    grouped_skills = {}
    skills = Tag.objects.filter(student=profile_user)

    for skill in skills:
        category = skill.category if isinstance(skill.category, str) else "Без категории"

        if category not in grouped_skills:
            grouped_skills[category] = []

        if skill.name:
            grouped_skills[category].append({
                'name': skill.name,
                'level': skill.level or '',
                'verified': getattr(skill, 'verified', False)
            })

    context = {
        'profile_user': profile_user,
        'grouped_skills': grouped_skills
    }

    return render(request, 'app/profile.html', context)