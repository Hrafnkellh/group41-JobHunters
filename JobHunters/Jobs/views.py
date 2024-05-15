from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from Users.models import Employer
from django.contrib.auth.decorators import login_required
from Jobs.models import JobListing
from Jobs.forms.contact_information_form import ContactInformationForm
from Jobs.forms.cover_letter_form import CoverLetterForm
from Jobs.forms.experiences_form import ExperiencesForm
from Jobs.forms.recommendations_form import RecommendationsForm
from Users.models import Employer, JobSeeker

# Create your views here.
def index(request):
    return render(request, 'Jobs/index.html' )

def frontpage(request):
    filter_by = request.GET.get('filter', None)

    if filter_by == 'title':
        job_listings = JobListing.objects.all().order_by('title')
    elif filter_by == 'employer':
        job_listings = JobListing.objects.all().order_by('employer__name')
    elif filter_by == 'salary':
        job_listings = JobListing.objects.all().order_by('-salary')
    else:
        job_listings = JobListing.objects.all()

    return render(request, 'Jobs/frontpage.html', context={ 'job_listings': job_listings})

def aboutUs(request):
    return render(request, 'Jobs/about_us.html')

def faq(request):
    return render(request, 'Jobs/faq.html')

def jobTips(request):
    return render(request, 'Jobs/job_tips.html')

def employers(request):
    return render(request, 'Jobs/employers.html', context={
        'employers': Employer.objects.all()
    })

def jobDetails(request, id):
    return render(request, 'Jobs/job_details_site.html', context={
        'job_listing': get_object_or_404(JobListing, pk=id)
    })

@login_required

def jobApplicationPage1Contact(request,id):
    jobseeker = JobSeeker.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ContactInformationForm(data=request.POST)
        form1 = RecommendationsForm(data=request.POST)
        form2 = ExperiencesForm(data=request.POST)
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            form.save()
            form1.save()
            form2.save()
            return render('jobApplicationn')
            #return redirect('log_in')
    url = reverse('jobApplicationn', kwargs={'id': id})
    return render(request, 'Jobs/job_application_page1_contact.html', {
        'form': ContactInformationForm(),
        'form1': RecommendationsForm(),
        'form2': ExperiencesForm(),
        'my_url': url
    })

def jobApplicationPage2Cover(request,id):
    if request.method == 'POST':
        form3 = CoverLetterForm(data=request.POST)
        if form3.is_valid():
            form3.save()
            return render('jobApplication3')
            #return redirect('log_in')
    url1 = reverse('jobApplication3', kwargs={'id': id})
    return render(request, 'Jobs/job_application_page2_cover.html', {
        'form3': CoverLetterForm(),
        'my_url1': url1
    })

def jobApplicatonPage3(request, id):
    return render(request,'Jobs/job_application_page3_expRec.html', {
        'JobListing': get_object_or_404(JobListing, pk=id)
    })
