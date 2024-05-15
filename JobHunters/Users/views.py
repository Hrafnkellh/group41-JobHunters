from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from Jobs.models import JobApplication, JobListing
from Users.forms.profile_form import ProfileForm
from Users.models import Employer, Profile, JobSeeker


# Create your views here.
def index(request):
    return render(request, 'Users/index.html' )

def logIn(request):
    return render(request, 'Users/log_in.html' )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            JobSeeker.objects.create(user=new_user)
            return redirect('log_in')
    return render(request, 'Users/sign_up.html', {'form': UserCreationForm()})

@login_required
def profile(request):
    profile = request.user
    jobseeker = JobSeeker.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=jobseeker, data=request.POST)
        if form.is_valid():
            jobseeker = form.save(commit=True)
            jobseeker.user = request.user
            jobseeker.save()
            return redirect('profile')
    return render(request, 'Users/profile.html', {
        'form': ProfileForm(instance=jobseeker),'user': request.user, 'jobseeker': jobseeker, 'applications': JobApplication.objects.filter(job_seeker=jobseeker)
        })


def employerDetails(request, id):
    return render(request, 'users/employer_details_site.html', context={
        'employer': get_object_or_404(Employer, pk=id), 'job_listings': JobListing.objects.filter(employer_id = id)
    })

@login_required
def applicationDetails(request, id):
    return render(request, 'Users/application_details_site.html', context={
        'application': get_object_or_404(JobApplication, job_seeker_id=request.user.id, job_listing_id=id)
    })