from django import forms

class ExperiencesForm(forms.Form):
    id = forms.IntegerField()
    place_of_work = forms.CharField()
    role = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    job_application_id = forms.IntegerField()
    