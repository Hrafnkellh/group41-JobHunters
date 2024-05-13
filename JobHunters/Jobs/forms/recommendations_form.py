from django import forms

class RecommendationsForm(forms.Form):
    text = forms.CharField()
    