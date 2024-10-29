from django import forms
from .models import Tag, SkillCategory

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'category', 'level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название навыка'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('', 'Выберите уровень'),
                (1, 'Начинающий'),
                (2, 'Средний'),
                (3, 'Продвинутый'),
                (4, 'Эксперт'),
            ])
        }

