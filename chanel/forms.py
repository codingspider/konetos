from django import forms
from .models import Channel


class ChannelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChannelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Channel
        fields = [
            'name', 'profile', 'description', 'cover', 'status', 'category'
        ]

