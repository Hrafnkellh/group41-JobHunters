from django import forms
#experience form 
class ExperiencesForm(forms.Form):
    place_of_work = forms.CharField(max_length=100, required=True)
    role = forms.CharField(max_length=100, required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    def __init__(self, *args, **kwargs):
        super(ExperiencesForm, self).__init__(*args, **kwargs)
        #apearence of experience.
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
