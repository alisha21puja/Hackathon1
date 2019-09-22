from django.db import models

# Create your models here.
from Organizer.models import OrganiseEvent
from django.contrib.auth.models import User


class SponsorTransaction(models.Model):
    spnsortype = models.CharField(max_length=100)
    org_id = models.OneToOneField(OrganiseEvent, on_delete=models.CASCADE)
    amount = models.IntegerField()
    us = models.OneToOneField(User, on_delete=models.CASCADE)
