from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name','image','description','price','category'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Product name'}),
            'price': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Product Price'}),
            # 'category': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Product Price'}),
            'description': forms.Textarea(attrs={'class' : 'form-control','rows':'3'}),
        }

