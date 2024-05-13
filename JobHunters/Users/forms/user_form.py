from django.forms import ModelForm, widgets
from django import forms
from Users.models import User


class UserLogInForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;'}))
    password = forms.PasswordInput()