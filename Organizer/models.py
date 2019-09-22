from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.utils.timezone import now
from django.utils import timezone
# from froala_editor.fields import FroalaField

from django.contrib.auth import get_user_model
# Create your models here.
# from .models import OrganiseEvent

class OrganiseEvent(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.CharField(max_length=800)
    event_category = models.CharField(max_length=200)
    org_name = models.CharField(max_length=200)
    org_email = models.EmailField(max_length=100)
    org_mobile = models.BigIntegerField()
    org_contact_person = models.CharField(max_length=100)
    event_poster = models.ImageField(
        upload_to='images/event_poster/', default="images/noimage.png")
    event_startdate = models.DateTimeField(default=now)
    event_enddate = models.DateTimeField()
    us = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.event_description[:150]


class EventDetails(models.Model):
    event = models.CharField(max_length=200)
    expected_participant = models.IntegerField()
    no_participant = models.IntegerField()
    event_level = models.CharField(max_length=200)
    eligibility = models.CharField(max_length=200)
    prerequisite = models.TextField(max_length=1500)
    facility = models.CharField(max_length=100)
    event_detail_docs = models.FileField(
        upload_to='images/event_details_docs/')
    us = models.ForeignKey(User,  on_delete=models.CASCADE)
    org_id = models.ForeignKey(OrganiseEvent, on_delete=models.CASCADE)


class ShareResource(models.Model):
    event_title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)
    publishedDate = models.DateTimeField(default=now)
    resourceLink = models.CharField(max_length=100)
    documentFile = models.FileField(upload_to='images/shared_resources_docs/')
    publisedBy = models.CharField(max_length=100)
    resourceImage = models.ImageField(upload_to='images/shared_resources/')
    us = models.ForeignKey(User,  on_delete=models.CASCADE)
    org_id = models.ForeignKey(OrganiseEvent, on_delete=models.CASCADE)


class SponsorShip(models.Model):
    event_title = models.CharField(max_length=100, default=True)
    platinum_sponsor = models.CharField(max_length=100)
    f_platinum = models.TextField(max_length=1500)
    ex_platinum = models.IntegerField()
    gold_sponsor = models.CharField(max_length=100)
    f_gold = models.TextField(max_length=1500)
    ex_gold = models.IntegerField()
    silver_sponsor = models.CharField(max_length=100)
    f_silver = models.TextField(max_length=1500)
    ex_silver = models.IntegerField()
    us = models.ForeignKey(User, on_delete=models.CASCADE)
    org_id = models.ForeignKey(OrganiseEvent, on_delete=models.CASCADE)


class Event_Location(models.Model):
    event_venue_name = models.CharField(max_length=200)
    event_venue_addr = models.CharField(max_length=300)
    event_latitude = models.CharField(max_length=100)
    event_longitude = models.CharField(max_length=100)
    eventid = models.ForeignKey(OrganiseEvent, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
