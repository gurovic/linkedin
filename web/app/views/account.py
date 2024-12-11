from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from app.forms.edit_account import EditAccountForm
from app.models import StudentSchool, UniversityStudent


@login_required
def editable_account_view(request, user_id):
    if user_id != request.user.id:
        return redirect("uneditable_account", user_id=user_id)

    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = EditAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("account", user_id=user.id)
    else:
        form = EditAccountForm(instance=user)
    return render(
        request,
        "app/editable_account.html",
        {
            "form": form,
            "user": user,
        },
    )


def uneditable_account_view(request, user_id):
    user = User.objects.get(id=user_id)
    student_schools_list = StudentSchool.objects.filter(student=user)
    student_universities_list = UniversityStudent.objects.filter(student=user)
    return render(
        request,
        "app/uneditable_account.html",
        {
            "user": user,
            "student_schools": student_schools_list,
            "student_universities": student_universities_list,
        },
    )
