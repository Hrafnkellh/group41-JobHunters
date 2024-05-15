from django import forms

class log_in_form(forms.Form):
    username = forms.CharField(max_length=16, min_length=4)
    password = forms.CharField(widget=forms.PasswordInput, max_length=22, min_length=8)

    def __init__(self, *args, **kwargs):
        super(log_in_form, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username',
            'style': 'width: 300px;'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'width: 300px;'
        })