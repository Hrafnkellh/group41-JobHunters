from django import forms

class CoverLetterForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True, label=False)

    def __init__(self, *args, **kwargs):
        super(CoverLetterForm, self).__init__(*args, **kwargs)

        self.fields['text'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': ' ',
            'contenteditable': 'true',
            'style': 'width: 1200px; word-wrap: break-word; word-break: break-all; display: inline;',
        })