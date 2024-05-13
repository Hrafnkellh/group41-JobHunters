from django import forms

class CoverLetterForm(forms.Form):
    text = forms.CharField()
    