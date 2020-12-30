from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Campaign


class CampaignForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CampaignForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Campaign
        fields = ['title', 'company', 'description', 'budget', 'status', 'end', 'gender', 'placement', 'bidding', 'url', 'page', 'audience', 'start', 'image']
        widgets = {
            'start': DatePickerInput(format='%Y-%m-%d'),
            'end': DatePickerInput(format='%Y-%m-%d'),
        }
