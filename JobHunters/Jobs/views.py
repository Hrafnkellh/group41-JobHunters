from django.shortcuts import redirect, render
from django.http import HttpResponse

from JobHunters.Jobs.forms.contact_information_form import ContactInformationForm
from JobHunters.Jobs.forms.cover_letter_form import CoverLetterForm
from JobHunters.Jobs.forms.experiences_form import ExperiencesForm
from JobHunters.Jobs.forms.recommendations_form import RecommendationsForm

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

def job_application_page1_contact(request):
    if request.method == 'POST':
        form = ContactInformationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return
            #return redirect('log_in')
    return render(request, 'Jobs/job_application_page1_contact.html', {
        'form': ContactInformationForm()
    })

def job_application_page2_cover(request):
    if request.method == 'POST':
        form = CoverLetterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return
            #return redirect('log_in')
    return render(request, 'Jobs/job_application_page2_cover.html', {
        'form': ContactInformationForm()
    })

def job_application_page3_exprec(request):
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