from django import forms
from django.contrib.auth.models import User


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Логин"
        self.fields["email"].label = "Email"

