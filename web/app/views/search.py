from django.contrib.auth.models import User
from django.shortcuts import render

from app.forms.search_form import (
    UserSearchForm,
)


def user_search(request):
    form = UserSearchForm(request.GET or None)
    users = User.objects.all()

    if (
        form.is_valid()
    ):
        query = form.cleaned_data.get("query")
        university = form.cleaned_data.get("university")
        school = form.cleaned_data.get("school")

        if query:
            users = users.filter(
                last_name__icontains=query,
            ) | users.filter(
                first_name__icontains=query,
            ) | users.filter(
                first_name__icontains=query.split(" ")[0],
            ) | users.filter(
                last_name__icontains=query.split(" ")[0],
            ) | users.filter(
                first_name__icontains=query.split(" ")[-1],
            ) | users.filter(
                last_name__icontains=query.split(" ")[-1],
            )

        if university:
            users = users.filter(student__university=university)
        if school:
            users = users.filter(schoolstudent__school=school)

    return render(
        request,
        "app/user_search.html",
        {
            "form": form,
            "users": users,
        },
    )
