from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ..models.unauthorised_alumni import UnauthorisedAlumni


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")


class AlumniForm(forms.ModelForm):
    class Meta:
        model = UnauthorisedAlumni
        fields = ["university", "graduation_year"]
        # widgets = {
        #     'university': forms.TextInput(),
        #     'graduation_year': forms.IntegerField(min_value=2021, max_value=2108)
        # }

    def clean(self):
        pass
