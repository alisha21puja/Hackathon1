from django.db import models

# Create your models here.




class Slider(models.Model):

	slide1=models.ImageField(upload_to='images/slider/')
	slide2=models.ImageField(upload_to='images/slider/')
	slide3=models.ImageField(upload_to='images/slider/')



class OurPartner(models.Model):
	organisationName = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	maplocation= models.CharField(max_length=600)	
	orgLogo = models.ImageField(upload_to='images/OurPartner/',default =True)
	

	


	