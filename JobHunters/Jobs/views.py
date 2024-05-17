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


    search_title = request.GET.get('search_title')
    starting_date = request.GET.get('starting_date')
    due_date = request.GET.get('due_date')
    time_type = request.GET.get('time_type')
    category = request.GET.get('category')
    sort = request.GET.get('sort', '')
    applied = request.GET.get('applied', '')
    is_remote = request.GET.get('is_remote')

    if search_title:
        job_listings = job_listings.filter(title__icontains=search_title)
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

    if applied:
        job_listing_id_list = list(job_applications.values_list('job_seeker_id', flat=True))
        job_listings = job_listings.filter(id__in=job_listing_id_list)


    for job in job_listings:
        job.salary_display = normalize_salary(job.salary)

    if sort == 'applied':
        job_listings = job_listings.order_by("jobapplication__job_seeker__user_id")

    if sort == 'starting_date':
        job_listings = job_listings.order_by("starting_date")

    if sort == 'due_date':
        job_listings = job_listings.order_by("due_date")

    if sort == '-starting_date':
        job_listings = job_listings.order_by("-starting_date")

    if sort == '-due_date':
        job_listings = job_listings.order_by("-due_date")

    else:
        # TODO: Setup default sorting
        print()

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
def jobApplication(request, id):
    # check if the job listing the application is for exists
    job_listing = get_object_or_404(JobListing, pk=id)

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

            return render(request, 'Jobs/index.html' )

    return render(request, 'Jobs/job_application_page.html', context={
        'form_contact': ContactInformationForm(prefix='contact'),
        'form_cover_letter': CoverLetterForm(prefix='cover'),
        'form_experience': ExperiencesForm(prefix='exp'),
        'form_recommendations': RecommendationsForm(prefix='rec')
    })

"""
@login_required

def JAP_1_1(request,id):
    print(request.method)
    if request.method == 'POST':
        form = ContactInformationForm()
        form1 = RecommendationsForm(data=request.POST)
        form2 = ExperiencesForm(data=request.POST)
        form3 = CoverLetterForm(data=request.POST)
        print("its a post malone1_1")
        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form1.save()
            form2.save()
            form3.save()
            return render('JobApp_1_2',form)
            #return redirect('log_in')

    url = reverse('jobApp_1_2', kwargs={'id': id})
    return render(request, 'Jobs/JAP_1_1.html', {
        'form': ContactInformationForm(),
        'my_url': url
    })

def JAP_1_2(request,id,form):
    print(request.method)
    if request.method == 'POST':
        form1 = RecommendationsForm(data=request.POST)
        print("its a post malone")
        if form1.is_valid():
            form1.save()
            return render('JobApp_1_3',form,form1)
            #return redirect('log_in')

    url = reverse('jobApp_1_3', kwargs={'id': id})
    return render(request, 'Jobs/JAP_1_2.html', {
        'form1': RecommendationsForm(),
        'my_url': url
    })

def JAP_1_3(request,id,form,form1):
    print(request.method)
    if request.method == 'POST':
        form2 = ExperiencesForm(data=request.POST)
        print("its a post malone")
        if form2.is_valid():
            form2.save()
            return render('jobApplicationn')
            #return redirect('log_in')

    url = reverse('jobApplicationn', kwargs={'id': id})
    return render(request, 'Jobs/JAP_1_3.html', {
        'form': ExperiencesForm(),
        'my_url': url
    })
   

@login_required
def jobApplicationPage1Contact(request,id):
    print(request.method)
    if request.method == 'POST':
        form = ContactInformationForm(data=request.POST)
        form2 = RecommendationsForm(data=request.POST)
        form1 = ExperiencesForm(data=request.POST)
        print("its a post malone")
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            form.save()
            form1.save()
            form2.save()
            return render('jobApplicationn')
            #return redirect('log_in')

    url = reverse('jobApplicationn', kwargs={'id': id})
    return render(request, 'Jobs/job_application_page1_contact.html', {
        'form': ContactInformationForm(),
        'form1': ExperiencesForm(),
        'form2': RecommendationsForm(),
        'my_url': url
    })

def jobApplicationPage2Cover(request,id):
    sad = get_object_or_404(JobListing, pk = id)
    jobseeker = JobSeeker.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form3 = CoverLetterForm(data=request.POST)
        if form3.is_valid():
            form3.save()
            new_jobApplication = JobApplication.objects.create(job_Seeker=jobseeker, job_listing=sad)
        
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
 """