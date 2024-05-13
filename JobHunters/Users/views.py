from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from Users.forms.profile_form import ProfileForm
from Users.models import Profile

# Create your views here.
def index(request):
    return render(request, 'Users/index.html' )

def log_in(request):
    return render(request, 'Users/log_in.html' )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request, 'Users/sign_up.html', {
        'form': UserCreationForm()
    })

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user.id).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user.id
            profile.save()
            return redirect('profile')
    return render(request, 'Users/profile.html', {
        'form': ProfileForm(instance=profile)
    })
