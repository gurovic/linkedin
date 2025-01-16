from django import forms
from ..models import UniversityStudent


class UniversityStudentForm(forms.ModelForm):
    class Meta:
        model = UniversityStudent
        fields = "__all__"