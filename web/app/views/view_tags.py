from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from app.models import Tag, UserTag


class AddTagForm(forms.Form):
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.none(),
        label="Выберите тег",
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['tag'].queryset = Tag.objects.exclude(usertags__user=user)


@login_required
def add_tag_to_user(request):
    user = get_object_or_404(User, id=request.user.id)

    if request.method == "POST":
        form = AddTagForm(request.POST, user=user)
        if form.is_valid():
            tag = form.cleaned_data["tag"]
            usertag = UserTag(user=user, tag=tag)
            usertag.save()
            return redirect("user_tags_old", user_id=user.id)
    else:
        form = AddTagForm(user=user)

    return render(request, "app/tags_form.html", {"item": user, "form": form})


def tags_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    usertags_list = user.usertags.all()
    context = {
        "usertags_list": usertags_list,
    }
    return render(request, "app/tags_list.html", context)
