from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class change_password_form(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(change_password_form, self).__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2',]:
            self.fields[fieldname].help_text = None

        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'width: 300px;'
        })

        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'width: 300px;'
        })

        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'width: 300px;'
        })
    class Meta:
        model = User
        fields = 'old_password', 'new_password1', 'new_password2'