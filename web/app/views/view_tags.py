from django.contrib.auth.models import User
from ..models import Tag
from django.shortcuts import render

def tags_view(request, user_id):
    user = User.objects.get(id = user_id)
    tags_list = user.tags.all()
    context = {
        'tags_list': tags_list
    }
    return render(request, 'app/tags_list.html', context)