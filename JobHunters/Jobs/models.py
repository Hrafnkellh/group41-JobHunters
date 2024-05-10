from django.db import models
from Users.models import Employer, JobSeeker

# Create your models here.
class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    salary = models.CharField(max_length=255)
    requirements = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    title = models.CharField(max_length=255)
    cover_letter = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, blank=False)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title
    
class Interview(models.Model):
    date_time = models.DateTimeField()

    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, blank=False)
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'{JobListing.title}: {JobApplication.title}\n{self.date_time}'
