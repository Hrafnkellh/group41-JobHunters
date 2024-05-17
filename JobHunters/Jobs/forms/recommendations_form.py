from django import forms

class RecommendationsForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email_address = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=False)
    role = forms.CharField(required=False)
    may_be_contacted = forms.BooleanField(required=False)
    def __init__(self, *args, **kwargs):
        super(RecommendationsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'full name',
            'style': 'width: 300px;'
        })
        self.fields['email_address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email',
            'style': 'width: 300px;'
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'phone number',
            'style': 'width: 300px;'
        })
        self.fields['role'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'role',
            'style': 'width: 300px;'
        })
        self.fields['may_be_contacted'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'may be contacted',
            'style': 'width: 300px;'
        })