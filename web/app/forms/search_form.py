from django import forms

from app.models import School, University


class UserSearchForm(forms.Form):
    university = forms.ModelChoiceField(
        queryset=University.objects.all(),
        required=False,
        label="University",
    )
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        required=False,
        label="School",
    )
    query = forms.CharField(required=False, max_length=60)
