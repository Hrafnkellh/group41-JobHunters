from django import forms

class ExperiencesForm(forms.Form):
    place_of_work = forms.CharField(max_length=100, required=True)
    role = forms.CharField(max_length=100)
    start_date = forms.DateField()
    end_date = forms.DateField()
    def __init__(self, *args, **kwargs):
        super(ExperiencesForm, self).__init__(*args, **kwargs)

        self.fields['place_of_work'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'place of work',
            'style': 'width: 300px;'
        })
        self.fields['role'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'role',
            'style': 'width: 300px;'
        })
        self.fields['start_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'start date',
            'style': 'width: 300px;'
        })
        self.fields['end_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'end date',
            'style': 'width: 300px;'
        })
