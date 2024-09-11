from django import forms


class CounterForm(forms.Form):
    counter = forms.CharField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'min': 1,
        'max': 99,
        'value': 1,
        'readonly': True
    }))