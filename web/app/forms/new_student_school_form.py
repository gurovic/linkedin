from django import forms
from ..models import StudentSchool

class StudentSchoolForm(forms.ModelForm):
    class Meta:
        model = StudentSchool
        fields = ['student', 'school', 'start_year', 'finish_year', 'why_left']
        widgets = {
            'student': forms.TextInput(attrs={'class': 'name_of_student'}),
            'school': forms.TextInput(attrs={'class': 'name_of_school'}),
            'start_year': forms.DateInput(attrs={'class': 'start_year_of_education'}),
            'finish_year': forms.DateInput(attrs={'class': 'finish_year_of_education'}),
            'why_left': forms.Select(attrs={'class': 'reason_of_leaving_school'}),
        }
