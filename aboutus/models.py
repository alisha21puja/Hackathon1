from django.db import models

from datetime import datetime
# Create your models here.

class OurServices(models.Model):
    serviceName = models.CharField(max_length=50)

class TeamInfo(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    profilePic = models.ImageField(upload_to='images/teamProfile')
    facebookLink = models.CharField(max_length=100)
    twitterLink = models.CharField(max_length=100)
    linkedInLink = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName

class AboutDescription(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/aboutusImage')

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
