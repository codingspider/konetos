import qs as qs
from django.forms import forms
from easy_select2 import Select2, Select2Multiple, apply_select2, admin, select2_modelform_meta
from .models import AutoFriend


class SomeModelForm(forms.ModelForm):
    Meta = select2_modelform_meta(AutoFriend)