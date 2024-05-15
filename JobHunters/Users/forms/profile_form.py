from django.forms import ModelForm, widgets
from Users.models import JobSeeker

class ProfileForm(ModelForm):
    class Meta:
        model = JobSeeker
        exclude = ['id', 'user_id', 'resume', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'profile_image_path': widgets.TextInput(attrs={'class': 'form-control', 'style': 'width: 800px'}),
            'address': widgets.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'email': widgets.TextInput(attrs={'class': 'form-control','style': 'width: 300px'}),
        }