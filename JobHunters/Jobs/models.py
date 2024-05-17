from django.db import models
from Users.models import Employer, JobSeeker

# Create your models here.
class JobListing(models.Model):
    title = models.CharField(max_length=255, default="undef")
    description = models.CharField(max_length=255, blank=True, default="undef")
    salary = models.CharField(max_length=255, default="undef")
    requirements = models.CharField(max_length=255, default="undef")
    category = models.CharField(max_length=255, default="undef")
    time_type = models.CharField(max_length=255, blank=True, default="undef")
    due_date = models.DateField(blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    is_remote = models.BooleanField(default=False)

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, blank=False,  default=0)

    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    title = models.CharField(max_length=255, default="undef")
    cover_letter = models.CharField(max_length=255, default="undef")
    status = models.CharField(max_length=255, default="undef")
    full_name = models.CharField(max_length=255, default="undef")
    street_name = models.CharField(max_length=255, default="undef")
    house_number = models.CharField(max_length=255, default="undef")
    city = models.CharField(max_length=255, default="undef")
    country = models.CharField(max_length=255, default="undef")
    postal_code = models.CharField(max_length=255, default="undef")

    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, blank=False,  default=0)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, blank=False,  default=0)

    def __str__(self):
        return self.title
    
class Interview(models.Model):
    date_time = models.DateTimeField()

    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, blank=False)
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'{JobListing.title}: {JobApplication.title}\n{self.date_time}'

class Experience(models.Model):
    place_of_work = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, blank=False)

class Recommendation(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    may_be_contacted = models.BooleanField()
    role = models.CharField(max_length=255)

    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, blank=False)
