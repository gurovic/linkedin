from django.contrib.admin.templatetags.admin_list import search_form
from django.shortcuts import render
from django.contrib.auth.models import User

from ..forms.search_form import UserSearchForm

def user_search(request):
    form = UserSearchForm(request.GET or None)
    match = []

    if form.is_valid():
        query = form.cleaned_data.get('query')

        users = User.objects.all()
        if query.strip() != "":
            for user in users:
                if query.lower() in (user.last_name + ' ' + user.first_name).lower() or\
                        query.lower() in (user.first_name + ' ' + user.last_name).lower():
                    match.append(user)

    return render(request, 'app/user_search.html', {'form': form, 'users': match})
