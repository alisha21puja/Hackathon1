from django.db import models

# Create your models here.
from django.utils.timezone import now


from django.contrib.auth.models import User


class BlogsInfo(models.Model):
    title = models.CharField(max_length=50)
    pubDateTime = models.DateTimeField(default=now)
    description = models.CharField(max_length=1000)
    imageSecond = models.ImageField(upload_to='images/blogsImages/')
    imageFirst = models.ImageField(upload_to='images/blogsImages/')
    UserType = models.CharField(max_length=30)
    authorName = models.CharField(max_length=30)
    blogCategory = models.CharField(max_length=30)
    refrenceLinks = models.CharField(max_length=30)
    us = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:175]
