from django import forms

class RecommendationsForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    email_address = forms.EmailField()
    phone_number = forms.IntegerField()
    role = forms.CharField()
    job_application_id = forms.IntegerField()

    may_be_contacted = forms.BooleanField()
    def __init__(self, *args, **kwargs):
        super(RecommendationsForm, self).__init__(*args, **kwargs)

        self.fields['id'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'id',
            'style': 'width: 300px;'
        })
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
        self.fields['job_application_id'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'job application id',
            'style': 'width: 300px;'
        })