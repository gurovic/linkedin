from django import forms
from ..models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'desc', 'country', 'majors_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name_of_school'}),
            'desc': forms.Textarea(attrs={'class': 'description_of_school'}),
            'country': forms.Select(attrs={'class': 'country_of_school'}),
            'majors_available': forms.CheckboxSelectMultiple(attrs={'class': 'major_of_school'}),
            }
