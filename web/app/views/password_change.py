from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms.password_change_form import PasswordChangeForm


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data.get('current_password')
            new_password = form.cleaned_data.get('new_password')

            # Verify the current password
            user = authenticate(username=request.user.username, password=current_password)
            if user:
                # Update the user's password
                user.set_password(new_password)
                user.save()

                # Re-authenticate and log the user back in
                login(request, user)
                messages.success(request, "Your password has been successfully changed.")
                return redirect('home')  # Redirect to a success page
            else:
                messages.error(request, "The current password is incorrect.")
    else:
        form = PasswordChangeForm()

    return render(request, 'app/change_password.html', {'form': form})
