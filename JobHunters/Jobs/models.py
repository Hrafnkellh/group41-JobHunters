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
    cover_letter = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    street_name = models.CharField(max_length=255, blank=True)
    house_number = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postal_code = models.IntegerField(blank=True, null=True)

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
    role = models.CharField(max_length=255, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, blank=False)

class Recommendation(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    may_be_contacted = models.BooleanField(blank=True)
    role = models.CharField(max_length=255, blank=True)

    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, blank=False)
