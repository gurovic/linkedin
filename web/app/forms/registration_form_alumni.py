from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ..models.alumni import Alumni


class RegistrationFormAlumni(UserCreationForm):

    class Meta:
        model = Alumni
        fields = ['username', 'email', 'password1', 'password2', 'graduation_year', 'university']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")