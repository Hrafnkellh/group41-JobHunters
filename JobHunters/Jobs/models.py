from django.db import models

# Create your models here.
class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    salary = models.CharField(max_length=255)
    requirements = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class JobApplication(models.model):
    title = models.CharField(max_length=255)
    cover_letter = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title
    
class Interview(models.model):
    date_time = models.DateTimeField()

    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, blank=False)
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'{JobListing.title}: {JobApplication.title}
        {self.date_time}'
