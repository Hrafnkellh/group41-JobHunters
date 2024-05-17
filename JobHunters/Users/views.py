from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from Jobs.models import Experience, JobApplication, JobListing, Recommendation
from Users.forms.change_password import change_password_form
from Users.forms.profile_form import ProfileForm
from Users.models import Employer, Profile, JobSeeker
from Users.forms.UserCreationForm import CreationForm
from Users.forms.Sign_in_form import log_in_form

def index(request):
    return render(request, 'Users/index.html' )

def login_page(request):
    if request.method == 'POST':
        form = log_in_form(data=request.POST)
        # checks if the form was correctly filled.
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # use built in authentication to validate the input.
            user = authenticate(request, username=username, password=password)
            # if user is found.
            if user is not None:
                login(request, user)
                return redirect('profile')
    return render(request, 'Users/log_in.html', {'form': log_in_form()})

def register(request):
    if request.method == 'POST':
        form = CreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # creates new user labeled as jobseeker.
            JobSeeker.objects.create(user=new_user)
            return redirect('log_in')
    return render(request, 'Users/sign_up.html', {'form': CreationForm()})

@login_required
def profile(request):
    # find the user that is logged in.
    jobseeker = JobSeeker.objects.filter(user=request.user).first()
    if request.method == 'POST':
        # the form for editing the profile
        form = ProfileForm(instance=jobseeker, data=request.POST)
        if form.is_valid():
            # we had commit false but changed to commit true when fixing a problem and it has been working for us so we did not change back.
            jobseeker = form.save(commit=True)
            jobseeker.user = request.user
            jobseeker.save()
            return redirect('profile')
    return render(request, 'Users/profile.html', {
        # making sure all the neccesary context is available.
        'form': ProfileForm(instance=jobseeker),'user': request.user, 'jobseeker': jobseeker, 'applications': JobApplication.objects.filter(job_seeker=jobseeker)
        })


def employerDetails(request, id):
    return render(request, 'users/employer_details_site.html', context={
        'employer': get_object_or_404(Employer, pk=id), 'job_listings': JobListing.objects.filter(employer_id = id)
    })

@login_required
def applicationDetails(request, id):
    application = get_object_or_404(JobApplication, job_seeker_id=request.user.id, job_listing_id=id)
    return render(request, 'Users/application_details_site.html', context={
        'application': application,
        'experience': Experience.objects.filter(job_application_id=application.id).first(),
        'recommendation': Recommendation.objects.filter(job_application_id=application.id).first()
    })

@login_required
def change_user_password(request):
    if request.method == 'POST':
        # use a custom change password form which is based on django's change password form.
        form = change_password_form(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # makes the user stay logged in after changing the password.
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = change_password_form(request.user)
    return render(request, 'Users/change_password.html', {'form': form})

@login_required
def delete_application(request, id):
    # get the user that is requesting to delete their application.
    jobseeker = get_object_or_404(JobSeeker, user=request.user)
    # get the application from said user.
    application = get_object_or_404(JobApplication, id=id, job_seeker=jobseeker)
    if request.method == 'POST':
        application.delete()
        return redirect('profile')
    else:
        return redirect('profile')
