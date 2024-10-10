from copy import deepcopy

from django.contrib.auth.models import User
from ..models import Tag, TagUser
from django.shortcuts import render

class LinkTag:
    def __init__(self, name, link):
        self.name = name
        self.link = link

def tags_view(request):
    tags_list = []
    for user in User.objects.all():
        for tag_user in TagUser.objects.all():
            if tag_user.user.id == user.id:
                linktag = LinkTag(tag_user.tag.name, "/user/" + str(user.id))
                tags_list.append(deepcopy(linktag))

    context = {
        'tags_list': tags_list
    }
    return render(request, 'linkedin/tags_list.html', context)