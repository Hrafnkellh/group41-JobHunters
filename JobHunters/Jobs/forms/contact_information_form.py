from django import forms
from django_countries.fields import CountryField

class ContactInformationForm(forms.Form):
    full_name = forms.CharField()
    street_name = forms.CharField()
    house_number = forms.IntegerField()
    city = forms.CharField()
    country = CountryField(blank_label="select country")
    postal_code = forms.CharField()