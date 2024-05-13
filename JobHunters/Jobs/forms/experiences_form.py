from django import forms

class ExperiencesForm(forms.Form):
    text = forms.CharField()
    