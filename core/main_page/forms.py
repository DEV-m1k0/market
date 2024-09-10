from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'search',
        'id': 'search',
        'placeholder': 'Поиск'
    }))