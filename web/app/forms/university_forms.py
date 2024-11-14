from django import forms
from ..models import University, UniversityStudent


class UniversityStudentForm(forms.ModelForm):
    class Meta:
        model = UniversityStudent
        fields = "__all__"