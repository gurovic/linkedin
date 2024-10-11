from django import forms

from app.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description", "picture", "date", "location"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Event Name"}),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Event Description",
                }
            ),
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "Event Location",
                }
            ),
        }
