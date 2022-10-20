from django import forms
class DateForm(forms.Form):
    start=forms.DateField(widget=forms.DateInput(attrs={'type':'Date'}))
    end=forms.DateField(widget=forms.DateInput(attrs={'type':'Date'}))