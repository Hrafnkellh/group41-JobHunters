from django import forms

class CoverLetterForm(forms.Form):
    text = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(CoverLetterForm, self).__init__(*args, **kwargs)

        self.fields['text'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': ' ',
            'style': 'width: 1200px; height: 600px;',
        })