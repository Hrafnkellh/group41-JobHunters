from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Jobs/index.html' )

def frontpage(request):
    return render(request, 'Jobs/frontpage.html')

def aboutUs(request):
    return render(request, 'Jobs/aboutUs.html')

def faq(request):
    return render(request, 'Jobs/faq.html')

def jobTips(request):
    return render(request, 'Jobs/jobTips.html')