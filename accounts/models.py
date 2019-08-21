from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Registration(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=40)
    confirmPassword = models.CharField(max_length=40)
    mobile = models.BigIntegerField()
    userType = models.CharField(max_length=50, blank=True)
    # add is published and status active one!

class Article(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)

class UserProfile(models.Model):
    # u_id = models.IntegerField()
    type_usr = models.IntegerField()
    phone = models.CharField(max_length=15)
    profile_img=models.ImageField(upload_to='media/images/Profile/')

    def __str__(self):
        return self.phone


# class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #mobile = models.BigIntegerField(null=True)
 #   userType = models.CharField(max_length=30,null=True, blank=True)


# @receiver(post_save,sender=User)
# def create_user_profile(sender,instance,**kwargs):
#	Profile.objects.create(user=instance)
