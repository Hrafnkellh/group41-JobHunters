from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Jobs.models import JobListing
from Jobs.forms.contact_information_form import ContactInformationForm
from Jobs.forms.cover_letter_form import CoverLetterForm
from Jobs.forms.experiences_form import ExperiencesForm
from Jobs.forms.recommendations_form import RecommendationsForm

# Create your views here.
def index(request):
    return render(request, 'Jobs/index.html' )

def frontpage(request):
    return render(request, 'Jobs/frontpage.html', context= {
        'job_listings': JobListing.objects.all()
    })

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
        'job_listing': get_object_or_404(JobListing, pk=id)
    })


@login_required

def jobApplicationPage1Contact(request,id):
    if request.method == 'POST':
        form = ContactInformationForm(data=request.POST)
        form1 = RecommendationsForm(data=request.POST)
        form2 = ExperiencesForm(data=request.POST)
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            form.save()
            form1.save()
            form2.save()
            return redirect('jAP2')
            #return redirect('log_in')
    return render(request, 'Jobs/job_application_page1_contact.html', {
        'form': ContactInformationForm(),
        'form1': RecommendationsForm(),
        'form2': ExperiencesForm()
    })

def jobApplicationPage2Cover(request,id):
    if request.method == 'POST':
        form3 = CoverLetterForm(data=request.POST)
        if form3.is_valid():
            form3.save()
            return redirect('index')
            #return redirect('log_in')
    return render(request, 'Jobs/job_application_page2_cover.html', {
        'form3': CoverLetterForm()
    })

def jobApplicatonPage3(request, id):
    return render(request, 'Jobs/job_application_page3expRec.hmtl', context={
        'job_listing': get_object_or_404(JobListing, pk=id)
    })
