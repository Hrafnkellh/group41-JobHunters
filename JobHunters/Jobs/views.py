from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from Users.models import Employer
from Jobs.forms.contact_information_form import ContactInformationForm
from Jobs.forms.cover_letter_form import CoverLetterForm
from Jobs.forms.experiences_form import ExperiencesForm
from Jobs.forms.recommendations_form import RecommendationsForm

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

def jobDetails(request, id):
    return render(request, 'Jobs/job_details_site.html', context={
        get_object_or_404(Employer(), pk=id)
    })

def jobApplicationPage1Contact(request):
    if request.method == 'POST':
        form = ContactInformationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return
            #return redirect('log_in')
    return render(request, 'Jobs/job_application_page1_contact.html', {
        'form': ContactInformationForm()
    })

def jobApplicationPage2Cover(request):
    if request.method == 'POST':
        form = CoverLetterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return
            #return redirect('log_in')
    return render(request, 'Jobs/job_application_page2_cover.html', {
        'form': ContactInformationForm()
    })

def jobApplicationPage3ExpRec(request):
    if request.method == 'POST':
        form1 = RecommendationsForm(data=request.POST)
        form2 = ExperiencesForm(data=request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return
            #return redirect('log_in')
    return render(request, 'Jobs/job_application_page3_expRec.html', {
        'form1': RecommendationsForm(), 'form2' : ExperiencesForm()
    })