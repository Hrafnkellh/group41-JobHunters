from django import forms

class ExperiencesForm(forms.Form):
    id = forms.IntegerField()
    place_of_work = forms.CharField()
    role = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    job_application_id = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        super(ExperiencesForm, self).__init__(*args, **kwargs)

        self.fields['id'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'id',
            'style': 'width: 300px;'
        })
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
        self.fields['job_application_id'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'job application id',
            'style': 'width: 300px;'
        })