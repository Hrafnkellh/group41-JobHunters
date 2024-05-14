from django import forms

class RecommendationsForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    email_address = forms.EmailField()
    phone_number = forms.IntegerField()
    may_be_contacted = forms.BooleanField()
    role = forms.CharField()
    job_application_id = forms.IntegerField()
    