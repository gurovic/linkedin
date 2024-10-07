from django.http import HttpResponse
from django.template import loader

from ..models.Alumni import Alumni

def get_friends(request):
    # Как с реквестом получать id выпускника, чтобы найти его друзей?
    # А как взять только тех выпускников, которые учатся в интересном вузе? А где взять название этого вуза?
    friends = Alumni.objects.all()
    template = loader.get_template("app/friends_in_university.html")
    context = {
        'friends': friends,
    }
    return HttpResponse(template.render(context, request))