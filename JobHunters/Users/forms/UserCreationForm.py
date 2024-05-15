from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2',]:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'form-control',
            'placeholder':'Username',
            'maxlength':'16',
            'minlength':'4',
        })
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'password',
            'maxlength': '22',
            'minlength': '8',
        })
        self.fields['password2'].widget.attrs.update({
                'required': '',
                'name': 'password2',
                'id': 'password2',
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'password',
                'maxlength': '22',
                'minlength': '8',
        })
    class Meta:
        model = User
        fields = 'username', 'password1', 'password2'
