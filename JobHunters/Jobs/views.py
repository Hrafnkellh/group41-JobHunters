from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Users.models import Employer
from Jobs.models import Experience, JobListing, JobApplication, JobSeeker, Recommendation
from Jobs.forms.contact_information_form import ContactInformationForm
from Jobs.forms.cover_letter_form import CoverLetterForm
from Jobs.forms.experiences_form import ExperiencesForm
from Jobs.forms.recommendations_form import RecommendationsForm
from django.utils.dateparse import parse_date


# Create your views here.
def index(request):
    return render(request, 'Jobs/index.html' )


def frontpage(request):
    job_listings = JobListing.objects.all()
    job_applications = JobApplication.objects.filter(job_seeker_id = request.user.id)
    employers = Employer.objects.all()


    categories = list(dict.fromkeys(list(job_listings.values_list('category', flat=True))))
    categories = [category.title() for category in categories]

    search_title = request.GET.get('title')
    employer = request.GET.get('employer')
    starting_date = request.GET.get('starting_date')
    due_date = request.GET.get('due_date')
    time_type = request.GET.get('time_type')
    category = request.GET.get('category')
    sort = request.GET.get('sort', '')
    application_status = request.GET.get('application_status', '')
    is_remote = request.GET.get('is_remote')

    if search_title:
        job_listings = job_listings.filter(title__icontains=search_title)
    if employer:
        job_listings = job_listings.filter(employer_id__exact=employer)
    if starting_date:
        job_listings = job_listings.filter(starting_date__gte=parse_date(starting_date))
    if due_date:
        job_listings = job_listings.filter(due_date__lte=parse_date(due_date))
    if time_type:
        job_listings = job_listings.filter(time_type__iexact=time_type)
    if category:
        job_listings = job_listings.filter(category__iexact=category)
    if is_remote:
        job_listings = job_listings.filter(is_remote=bool(int(is_remote)))

    if application_status:
        job_listing_id_list = list(job_applications.values_list('job_listing_id', flat=True))
        if application_status == "1":
            job_listings = job_listings.filter(id__in=job_listing_id_list)
        if application_status == "0":
            job_listings = job_listings.exclude(id__in=job_listing_id_list)


    for job in job_listings:
        job.salary_display = normalize_salary(job.salary)

    if sort == 'starting_date':
        job_listings = job_listings.order_by("starting_date")

    if sort == 'due_date':
        job_listings = job_listings.order_by("due_date")

    if sort == '-starting_date':
        job_listings = job_listings.order_by("-starting_date")

    if sort == '-due_date':
        job_listings = job_listings.order_by("-due_date")

    return render(request, 'Jobs/frontpage.html', {
        'job_listings': job_listings,
        'employers': employers,
        'categories': categories
        })

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
    application_exists = JobApplication.objects.filter(job_listing_id=id, job_seeker_id=request.user.id).exists()
    return render(request, 'Jobs/job_details_site.html', context={
        'job_listing': get_object_or_404(JobListing, pk=id),
        'application_exists': application_exists,
    })

@login_required
def jobApplication(request, id):
    # check if the job listing the application is for exists
    job_listing = get_object_or_404(JobListing, pk=id)
    application_exists = JobApplication.objects.filter(job_listing_id=id, job_seeker_id=request.user.id).exists()

    if request.method == 'POST':
        contact_form = ContactInformationForm(request.POST, prefix='contact')
        cover_letter_form = CoverLetterForm(request.POST, prefix='cover')
        experience_form = ExperiencesForm(request.POST, prefix='exp')
        recommendations_form = RecommendationsForm(request.POST, prefix='rec')
        if contact_form.is_valid() and cover_letter_form.is_valid():
            new_job_application = JobApplication.objects.create(
                title=job_listing.title,
                cover_letter=cover_letter_form.cleaned_data['text'],
                status='processing',
                full_name=contact_form.cleaned_data['full_name'],
                street_name=contact_form.cleaned_data['street_name'],
                house_number=contact_form.cleaned_data['house_number'],
                city=contact_form.cleaned_data['city'],
                postal_code=contact_form.cleaned_data['postal_code'],
                country=contact_form.cleaned_data['country'],
                job_seeker_id=request.user.id,
                job_listing_id=job_listing.id
            )
            successes = ['Job Application creation succeeded']

            if experience_form.is_valid():
                Experience.objects.create(
                    place_of_work=experience_form.cleaned_data['place_of_work'],
                    role=experience_form.cleaned_data['role'],
                    start_date=experience_form.cleaned_data['start_date'],
                    end_date=experience_form.cleaned_data['end_date'],
                    job_application_id=new_job_application.id
                )
                successes.append('Experience has been recorded')

            if recommendations_form.is_valid():
                Recommendation.objects.create(
                    name=recommendations_form.cleaned_data['name'],
                    email_address=recommendations_form.cleaned_data['email_address'],
                    phone_number=recommendations_form.cleaned_data['phone_number'],
                    may_be_contacted=recommendations_form.cleaned_data['may_be_contacted'],
                    role=recommendations_form.cleaned_data['role'],
                    job_application_id=new_job_application.id
                )
                successes.append('Recommendation has been recorded')
            return render(request=request, template_name='Jobs/congratulations.html', context={
                'successes': successes
            })
    if application_exists:
        return redirect(to='jobDetails', id=id)
    return render(request, 'Jobs/job_application_page.html', context={
        'form_contact': ContactInformationForm(prefix='contact'),
        'form_cover_letter': CoverLetterForm(prefix='cover'),
        'form_experience': ExperiencesForm(prefix='exp'),
        'form_recommendations': RecommendationsForm(prefix='rec')
    })