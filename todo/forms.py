from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "details", "date")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project name'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Product date'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }