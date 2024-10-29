from django.contrib.auth.models import User
from ..models import Tag
from django.shortcuts import render, get_object_or_404, redirect
from django import forms

class AddTagForm(forms.Form):
    tag = forms.ModelChoiceField(queryset = Tag.objects.all(), label = "Выберите тег")

def add_tag_to_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = AddTagForm(request.POST)
        if form.is_valid():
            tag = form.cleaned_data['tag']
            user.tags.add(tag)
            return redirect(f"/app/tags/{ user.id }/")  # Предполагаем, что у вас есть detail-view для Item
    else:
        form = AddTagForm()

    return render(request, 'app/tags_form.html', {'item': user, 'form': form})

def tags_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tags_list = user.tags.all()
    context = {
        'tags_list': tags_list
    }
    return render(request, 'app/tags_list.html', context)