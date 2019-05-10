from django.db import models

# Create your models here.

class Slider(models.Model):

	slide1=models.ImageField(upload_to='images/')
	slide2=models.ImageField(upload_to='images/')
	slide3=models.ImageField(upload_to='images/')
	