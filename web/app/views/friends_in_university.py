from django.shortcuts import render

from ..models import Friend
from ..models import Profile

def get_friends(request):
    user = request.user
    edges = Friend.objects.filter(user1=user)
    context = {
        'edges': edges,
    }
    return render(request, "app/friends_in_university.html", context)
