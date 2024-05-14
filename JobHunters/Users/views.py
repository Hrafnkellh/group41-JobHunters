from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from Users.forms.profile_form import ProfileForm
from Users.models import Employer, Profile

# Create your views here.
def index(request):
    return render(request, 'Users/index.html' )

def logIn(request):
    return render(request, 'Users/log_in.html' )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request, 'Users/sign_up.html', {'form': UserCreationForm()})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            user.save()
            return redirect('profile')  # Adjust to your profile URL name
    else:
        form = ProfileForm(instance=user)

    return render(request, 'Users/profile.html', {'form': form})

def employersDetails(request, id):
    return render(request, 'Users.employer_details_site.html', context={
        'employer': get_object_or_404(Employer, pk=id)
    })