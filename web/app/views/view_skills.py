from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from app.models import Skill, UserSkill


class AddskillForm(forms.Form):
    skill = forms.ModelChoiceField(
        queryset=Skill.objects.none(),
        label="Выберите тег",
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['skill'].queryset = Skill.objects.exclude(userskills__user=user)


@login_required
def add_skill_to_user(request):
    user = get_object_or_404(User, id=request.user.id)

    if request.method == "POST":
        form = AddskillForm(request.POST, user=user)
        if form.is_valid():
            skill = form.cleaned_data["skill"]
            userskill = UserSkill(user=user, skill=skill)
            userskill.save()
            return redirect("user_skills_old", user_id=user.id)
    else:
        form = AddskillForm(user=user)

    return render(request, "app/skills_form.html", {"item": user, "form": form})


def skills_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    userskills_list = user.userskills.all()
    context = {
        "userskills_list": userskills_list,
    }
    return render(request, "app/skills_list.html", context)
