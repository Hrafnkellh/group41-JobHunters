from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class JobSeeker(User):
    resume = models.CharField(max_length = 255, blank = True)

    def __str__(self):
        return self.name
    
class Employer(User):
    esg_rating = models.IntegerField()
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.name