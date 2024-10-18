from django import forms
from ..models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['name', 'desc', 'approved']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name_of_request'}),
            'desc': forms.Textarea(attrs={'class': 'description_of_request'}),
            'approved': forms.CheckboxInput(attrs={'class': 'if_approved'}),
        }