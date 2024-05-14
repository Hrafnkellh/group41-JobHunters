from django.forms import ModelForm, widgets
from Users.models import JobSeeker

class ProfileForm(ModelForm):
    class Meta:
        model = JobSeeker
        exclude = ['id', 'user_id', 'resume', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image_path': widgets.FileInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
        }