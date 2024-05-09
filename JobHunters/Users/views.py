from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'Users/index.html' )

def register(request):
    return render(request, 'Users/sign_up.html' )

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
