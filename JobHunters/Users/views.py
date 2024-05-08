from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Users/index.html' )

def sign_up_index(request):
    return render(request, 'Users/sign_up.html' )

def log_in_index(request):
    return render(request, 'Users/log_in.html' )
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'Users/sign_up.html', {
        'form': UserCreationForm()
    })
