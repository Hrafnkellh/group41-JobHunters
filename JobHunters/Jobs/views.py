from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Jobs.models import JobListing, Employer, JobSeeker
from Jobs.forms.contact_information_form import ContactInformationForm
from Jobs.forms.cover_letter_form import CoverLetterForm
from Jobs.forms.experiences_form import ExperiencesForm
from Jobs.forms.recommendations_form import RecommendationsForm
from django.db.models.functions import Trim
from django.db.models.functions import Cast
from django.utils.dateparse import parse_date
from django.db.models import CharField

# Create your views here.
def index(request):
    return render(request, 'Jobs/index.html' )

def frontpage(request):
    job_listings = JobListing.objects.all()

    starting_date = request.GET.get('starting_date')
    due_date = request.GET.get('due_date')
    time_type = request.GET.get('time_type')
    category = request.GET.get('category')
    sort = request.GET.get('sort', '')


    if starting_date:
        job_listings = job_listings.filter(starting_date__gte=parse_date(starting_date))
    if due_date:
        job_listings = job_listings.filter(due_date__lte=parse_date(due_date))
    if time_type:
        job_listings = job_listings.filter(time_type__iexact=time_type)
    if category:
        job_listings = job_listings.filter(category__iexact=category)


    for job in job_listings:
        job.salary_display = normalize_salary(job.salary)

    if sort:
        job_listings = job_listings.order_by(sort)

    return render(request, 'Jobs/frontpage.html', { 'job_listings': job_listings})

def normalize_salary(salary_str):
    try:
        if 'per hour' in salary_str:
            hourly_rate = float(salary_str.split()[0])
            annual_salary = hourly_rate * 40 * 52
            return f"${annual_salary:,.0f} per year"
        elif '-' in salary_str:
            parts = salary_str.split('-')
            low = float(parts[0].replace('$', '').replace('K', '000').strip())
            high = float(parts[1].replace('$', '000').replace('K', '000').strip())
            return f"${low:,.0f} - ${high:,.0f} per year"
        elif 'K' in salary_str:
            return f"${float(salary_str.replace('K', '000').replace('$', '').strip()):,.0f} per year"
        elif 'M' in salary_str:
            return f"${float(salary_str.replace('M', '000000').replace('$', '').strip()):,.0f} per year"
        return salary_str
    except ValueError:
        return salary_str

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
