from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title','description','short_description','thumbnail'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Title'}),
            'short_description': forms.Textarea(attrs={'class' : 'form-control','rows':'3'}),
            'description': forms.Textarea(attrs={'class' : 'form-control','rows':'10'}),
        }
