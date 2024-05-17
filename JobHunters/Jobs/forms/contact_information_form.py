from django import forms

class ContactInformationForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    street_name = forms.CharField(max_length=120, required=True)
    house_number = forms.IntegerField(max_value=999, required=True)
    city = forms.CharField(max_length=100, required=True)
    postal_code = forms.CharField(max_length=5, required=True)
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