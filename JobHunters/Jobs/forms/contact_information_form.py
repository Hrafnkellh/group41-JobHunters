from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

#contact information form
class ContactInformationForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget())
    street_name = forms.CharField(max_length=120, required=True)
    house_number = forms.CharField(max_length=10, required=True)
    city = forms.CharField(max_length=100, required=True)
    postal_code = forms.CharField(max_length=5, required=True)
    def __init__(self, *args, **kwargs):
        super(ContactInformationForm, self).__init__(*args, **kwargs)
        #styles and apearance for evey field in contact form.
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'full name',
            'style': 'width: 300px;'
        })
        self.fields['country'].widget.attrs.update({
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