from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class JobSeeker(models.Model):
    name = models.CharField(max_length = 255, blank= True)
    email = models.EmailField(max_length = 255, blank= True)
    resume = models.CharField(max_length = 255, blank = True)
    profile_image_path = models.CharField(max_length=255, blank = True)
    address = models.CharField(max_length=255, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employer(models.Model):
    name = models.CharField(max_length = 255, blank= True)
    email = models.EmailField(max_length = 255, blank = True)
    esg_rating = models.IntegerField(null=True)
    address = models.CharField(max_length=255)
    logo_path = models.CharField(max_length = 255, blank = True)
    cover_image_path = models.CharField(max_length = 255, blank = True)
    description = models.CharField(max_length = 255, blank = True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    profile_image_path = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.user
"""
employer = Employer.objects.create(
    esg_rating=80,
    address="Grensásvegur 12",
    logo_path="pics/advaniaLogo.png",
    cover_image_path="pics/advaniaCoverImage.png",
    description="We are a tech company looking to hire the finest of people on this mother earth. Thank you."
)""" 