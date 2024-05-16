from django import forms
from django_countries.fields import CountryField

class ContactInformationForm(forms.ModelForm):
    full_name = forms.CharField()
    street_name = forms.CharField()
    house_number = forms.IntegerField()
    city = forms.CharField()
    country = CountryField(blank_label="select country")
    postal_code = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(ContactInformationForm, self).__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'full name',
            'style': 'width: 300px;'
        })
        self.fields['street_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Street Name',
            'style': 'width: 300px;'
        })
        self.fields['house_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '00',
            'style': 'width: 300px;'
        })
        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'City',
            'style': 'width: 300px;'
        })
        self.fields['postal_code'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '000',
            'style': 'width: 300px;'
        })