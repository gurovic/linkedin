from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)