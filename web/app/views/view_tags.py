from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from app.models import Skill, UserSkill


class AddSkillForm(forms.Form):
    tag = forms.ModelChoiceField(
        queryset=Skill.objects.none(),
        label="Выберите навык",
    )


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['skill'].queryset = Skill.objects.exclude(userskill__user=user)


@login_required
def add_skill_to_user(request):
    user = get_object_or_404(User, id=request.user.id)

    if request.method == "POST":
        form = AddSkillForm(request.POST, user=user)
        if form.is_valid():
            skill = form.cleaned_data["skill"]
            userskill = UserSkill(user=user, skill=skill)
            userskill.save()
            return redirect("user_skills_old", user_id=user.id)
    else:
        form = AddSkillForm(user=user)

    return render(request, "app/tags_form.html", {"item": user, "form": form})


def skill_view(request, user_id):
    user= get_object_or_404(User, id=user_id)
    userskill_list = user.userskills.all()
    context = {
        "usertags_list": userskill_list,
    }
    return render(request, "app/tags_list.html", context)
