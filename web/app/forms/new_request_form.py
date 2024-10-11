from django import forms
from ..models import requests

class RequestForm(forms.ModelForm):
    class Meta:
        model = requests
        fields = ['name', 'desc', 'date', 'right_asked', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name_of_request'}),
            'desc': forms.Textarea(attrs={'class': 'description_of_request'}),
            'date': forms.DateInput(attrs={'class': 'date_of_request'}),
            'right_asked': forms.Select(attrs={'class': 'right_asked_of_request'}),
            'user': forms.Select(attrs={'class': 'user_of_request'}),
        }
