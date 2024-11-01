# forms.py
from django import forms
from ..models import JobExperience

class JobExperienceForm(forms.ModelForm):
    class Meta:
        model = JobExperience
        fields = ['company_name', 'start_year', 'end_year', 'position']
        widgets = {
            'start_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
            'end_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }
