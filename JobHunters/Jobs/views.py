from django.shortcuts import redirect, render
from django.http import HttpResponse

from JobHunters.Jobs.forms.contact_information_form import ContactInformationForm

# Create your views here.
def index(request):
    return render(request, 'Jobs/index.html' )

def frontpage(request):
    return render(request, 'Jobs/frontpage.html')

def aboutUs(request):
    return render(request, 'Jobs/about_us.html')

def faq(request):
    return render(request, 'Jobs/faq.html')

def jobTips(request):
    return render(request, 'Jobs/job_tips.html')

def employers(request):
    return render(request, 'Jobs/employers.html')

def job_application_page1(request):
    if request.method == 'POST':
        form = ContactInformationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return
            #return redirect('log_in')
    return render(request, 'Jobs/job_application_page1_contact.html', {
        'form': ContactInformationForm()
    })