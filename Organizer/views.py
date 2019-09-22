from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import forms
from .models import OrganiseEvent, EventDetails, ShareResource, SponsorShip, Event_Location
from django.contrib.auth.models import User
from accounts.models import UserProfile
from Blog.models import BlogsInfo
from django.utils import timezone
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse,Http404
from wsgiref.util import FileWrapper
import os
from django.conf import settings
from Participant.models import ParticipateEvent
from Sponsor.models import SponsorTransaction

def participants_event(request,id):
    event = OrganiseEvent.objects.get(pk=id)
    try:
        participants = ParticipateEvent.objects.get(Event_id_id=id)
        usr = User.objects.get(pk=participants.us_id)
        otherdetails_usr = UserProfile.objects.get(id=participants.us_id)
        return render(request, 'participants_event.html', {'event': event, 'part': participants, 'usr': usr, 'otherdetails_usr': otherdetails_usr})
    except:
        return render(request, 'participants_event.html', {'event': event})


def sponser_for_event(request, id):
    event = OrganiseEvent.objects.get(pk=id)
    sponsor_id = SponsorTransaction.objects.get(org_id_id=id)
    sponsor = User.objects.get(pk=sponsor_id.us_id)
    otherdetails_usr = UserProfile.objects.get(id=sponsor_id.us_id)
    try:
        return render(request, 'sponsor_for_event.html', {'otherdetails_usr': otherdetails_usr,'sponsor': sponsor, 'event': event})
    except:
        return render(request, 'sponsor_for_event.html',{'event': event})

def EventLocation(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        event_venue_name = request.POST['venue_name']
        event_venue_addr = request.POST['venue_addr']
        event_latitude = request.POST['event_latitude']
        event_longitude = request.POST['event_longitude']

        if event_venue_name == '':
            return render(request, 'eventlocationinfo.html', {'error': "Event Venue is missing"})
        else:
            event_venue_name = request.POST['venue_name']
        if event_venue_addr == '':
            return render(request, 'eventlocationinfo.html', {'error': "Event Address is missing"})
        else:
            event_venue_addr = request.POST['venue_addr']
        if event_latitude == '':
            return render(request, 'eventlocationinfo.html', {'error': "Event Latitude is missing"})
        else:
            event_latitude = request.POST['event_latitude']
        if event_longitude == '':
            return render(request, 'eventlocationinfo.html', {'error': "Event longitude is missing"})
        else:
            event_longitude = request.POST['event_longitude']
        if event_name == '':
            return render(request, 'eventlocationinfo.html', {'error': "Event Name is missing"})
        else:
            event_name = request.POST['event_name']

        eid = OrganiseEvent.objects.get(event_title=event_name)
        location_data = Event_Location(event_venue_name=event_venue_name, event_venue_addr=event_venue_addr,
                                       event_latitude=event_latitude, event_longitude=event_longitude, eventid_id=eid.id, event_name=event_name)
        location_data.save()

        return render(request, 'organiser_index.html')
    else:
        return render(request, 'eventlocationinfo.html')


def EventLocationload(request):
    event = OrganiseEvent.objects.filter(us=request.user.id)
    return render(request, 'eventlocationinfo.html', {'event': event})


def Location_view(request):
    event = OrganiseEvent.objects.filter(us=request.user.id)
    return render(request, 'locationinfo_view.html', {'event': event})


def load_map(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        event = OrganiseEvent.objects.filter(us=request.user.id)
        loc = Event_Location.objects.filter(event_name=event_name)
        return render(request, 'locationinfo_view.html', {'event': event, 'location': loc})
    else:
        event = OrganiseEvent.objects.filter(us=request.user.id)
        return render(request, 'locationinfo_view.html', {'event': event})

def locationupdate(request,id):
    # event = OrganiseEvent.objects.filter(us=request.user.id)
    # return render(request, 'locationinfo_view.html', {'event': event})
    if request.method == 'POST':
        evnt=Event_Location.objects.get(pk=id)
        event_venue_name = request.POST['event_venue_name']
        event_venue_addr = request.POST['event_venue_addr']
        event_latitude = request.POST['event_latitude']
        event_longitude = request.POST['event_longitude']
        event_name = request.POST['event_name']
        submitbutton = request.POST.get('Submit')
        if submitbutton:
            eid = OrganiseEvent.objects.get(event_title=event_name)
            location_data = Event_Location(id=id,event_venue_name=event_venue_name, event_venue_addr=event_venue_addr,
                                       event_latitude=event_latitude, event_longitude=event_longitude, eventid_id=eid.id, event_name=event_name)
            location_data.save()
            event = OrganiseEvent.objects.filter(us=request.user.id)
            return render(request, 'locationinfo_view.html', {'event': event,'error': "Successfully edited the details"})
        else:
            event = OrganiseEvent.objects.filter(us=request.user.id)
            return render(request, 'locationinfo_view.html', {'event': event})
    else:
        event = OrganiseEvent.objects.filter(us=request.user.id)
        return render(request, 'locationinfo_view.html', {'event': event})

def locationdelete(request,id):
    event = Event_Location.objects.get(pk=id)
    event.delete()
    event = OrganiseEvent.objects.filter(us=request.user.id)
    return render(request, 'locationinfo_view.html', {'event': event,'error': "Successfully removed the details"})

def editSponsorShip(request):
    sponsorShip = SponsorShip.objects.filter(us=request.user.id)
    return render(request, 'edit_sponsorship.html', {'sponsorShip': sponsorShip})


def deletesponsor(request, id):
    sponsorShip = SponsorShip.objects.get(id=id)
    sponsorShip.delete()
    sponsorShip = SponsorShip.objects.filter(us=request.user.id)
    return render(request, 'edit_sponsorship.html', {'sponsorShip': sponsorShip})


def deleteeventdetails(request, id):
    events = OrganiseEvent.objects.get(id=id)
    loc = Event_Location.objects.filter(eventid_id=request.user.id)
    events.delete()
    loc.delete()
    events = OrganiseEvent.objects.filter(us=request.user.id)
    loc = Event_Location.objects.filter(eventid_id=request.user.id)
    context = {'events': events, 'loc': loc}
    return render(request, 'registered_event.html', context)

def evenDetailsdelete(request,id):
    if request.method == 'POST':
        events = EventDetails.objects.get(pk=id)
        events.delete()
        eventDetails = EventDetails.objects.filter(us=request.user.id)
        eventsOrganise = OrganiseEvent.objects.filter(us=request.user.id)
        context = {	'eventDetails': eventDetails,
                    'eventsOrganise': eventsOrganise,
                    'registered': 'Event Details Removed!'
                    }
        return render(request, 'addrubrics.html', context)


def deleteresourcedetails(request,id):
    resource=ShareResource.objects.get(id=id)
    resource.delete()
    share_resource = ShareResource.objects.filter(us=request.user.id)
    return render(request, 'edit_shareresource.html', {'share_resource': share_resource})


def updateSponsorInfo(request,id):
    spon = SponsorShip.objects.get(pk=id)
    submitbutton = request.POST.get('Submit')
    if submitbutton:
        sponsor = SponsorShip.objects.get(pk=id)
        event_title = request.POST['event_title']
        platinum_sponsor = request.POST['platinum_sponsor']
        f_platinum = request.POST['f_platinum']
        ex_platinum = request.POST['ex_platinum']
        gold_sponsor = request.POST['gold_sponsor']
        f_gold = request.POST['f_gold']
        ex_gold = request.POST['ex_gold']
        silver_sponsor = request.POST['silver_sponsor']
        f_silver = request.POST['f_silver']
        ex_silver = request.POST['ex_silver']
        userr = User.objects.get(pk= request.user.id)      
        orgid = OrganiseEvent.objects.get(id=spon.org_id.id)
        sponsor_ship = SponsorShip(id=id, event_title=event_title, platinum_sponsor=platinum_sponsor, f_platinum=f_platinum, ex_platinum=ex_platinum, gold_sponsor=gold_sponsor,
                                   f_gold=f_gold, ex_gold=ex_gold, silver_sponsor=silver_sponsor, f_silver=f_silver, ex_silver=ex_silver, us=userr,org_id=orgid)
        sponsor_ship.save()
        sponsorShip = SponsorShip.objects.filter(us=request.user.id)
        return render(request, 'edit_sponsorship.html', {'sponsorShip': sponsorShip})
    else:
        if platinum_sponsor == '':
            return render(request, 'edit_sponsorship.html', {'error': "Title is not given"})
        else:
            platinum_sponsor = request.POST['platinum_sponsor']
        if f_platinum == '':
            return render(request, 'edit_sponsorship.html', {'error': "Title is not given"})
        else:
            f_platinum == request.POST['f_platinum']
        if ex_platinum == '':
            return render(request, 'edit_sponsorship.html', {'error': "Title is not given"})
        else:
            ex_platinum = request.POST['ex_platinum']
        if gold_sponsor == '':
            return render(request, 'edit_sponsorship.html', {'error': "Title is not given"})
        else:
            gold_sponsor = request.POST['gold_sponsor']
        if f_gold == '':
            return render(request, 'edit_sponsorship.html', {'error': "Title is not given"})
        else:
            f_gold = request.POST['f_gold']
        if ex_gold == '':
            return render(request, 'edit_sponsorship.html', {'error': "Title is not given"})
        else:
            ex_gold = request.POST['ex_gold']
        if silver_sponsor == '':
            return render(request, 'edit_sponsorship.html', {'error': "Title is not given"})
        else:
            silver_sponsor = request.POST['silver_sponsor']
        if f_silver == '':
            return render(request, 'edit_sponsorship.html', {'error': "Title is not given"})
        else:
            f_silver = request.POST['f_silver']
        if ex_silver == '':
            return render(request, 'edit_sponsorship.html', {'error': "Title is not given"})
        else:
            ex_silver = request.POST['ex_silver']

def sponsorShip(request):
    event = OrganiseEvent.objects.filter(us_id=request.user.id)
    return render(request, 'sponsorShip.html', { 'event': event})


def sponsorShipDetails(request):
    if request.method == 'POST':
        eventDetail = EventDetails.objects.filter(us=request.user.id)
        event = request.POST['event_title']
        event_title = request.POST['event_title']
        platinum_sponsor = request.POST['platinum_sponsor']
        f_platinum = request.POST['f_platinum']
        ex_platinum = request.POST['ex_platinum']
        gold_sponsor = request.POST['gold_sponsor']
        f_gold = request.POST['f_gold']
        ex_gold = request.POST['ex_gold']
        silver_sponsor = request.POST['silver_sponsor']
        f_silver = request.POST['f_silver']
        ex_silver = request.POST['ex_silver']

        if platinum_sponsor == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            platinum_sponsor = request.POST['platinum_sponsor']
        if f_platinum == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            f_platinum == request.POST['f_platinum']
        if ex_platinum == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            ex_platinum = request.POST['ex_platinum']
        if gold_sponsor == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            gold_sponsor = request.POST['gold_sponsor']
        if f_gold == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            f_gold = request.POST['f_gold']
        if ex_gold == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            ex_gold = request.POST['ex_gold']
        if silver_sponsor == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            silver_sponsor = request.POST['silver_sponsor']
        if f_silver == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            f_silver = request.POST['f_silver']
        if ex_silver == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            ex_silver = request.POST['ex_silver']

        orgid = OrganiseEvent.objects.get(event_title=event_title)
        sponsor_ship = SponsorShip(event_title=event, platinum_sponsor=platinum_sponsor, f_platinum=f_platinum, ex_platinum=ex_platinum, gold_sponsor=gold_sponsor,
                                   f_gold=f_gold, ex_gold=ex_gold, silver_sponsor=silver_sponsor, f_silver=f_silver, ex_silver=ex_silver, us_id=request.user.id, org_id=orgid)
        sponsor_ship.save()
        event = OrganiseEvent.objects.filter(us_id=request.user.id)
        return render(request, 'sponsorShip.html', {'event': event})


def blogsDetails(request):
    blogsInfo = BlogsInfo.objects.filter(us=request.user.id)
    return render(request, 'blog_edit.html', {'blogsInfo': blogsInfo})


def blog(request):
    blogsInfo = BlogsInfo.objects.filter(us=request.user.id)
    return render(request, 'blog_write.html', {'blogsInfo': blogsInfo})


def view_org_blog(request):
    blogsInfo = BlogsInfo.objects.filter(us=request.user.id)
    return render(request, 'view_org_blog.html', {'blogsInfo': blogsInfo})


def writeBlogs(request):
    if request.method == 'POST':
        title = request.POST['blog_title']
        pubDateTime = timezone.now()
        description = request.POST['description']
        imageSecond = request.POST['image_second']
        imageFirst = request.POST['image_first']
        blogCategory = request.POST['blog_category']
        refrenceLinks = request.POST['refrence_link']
        UserType = 'Organiser'
        if request.user.is_authenticated:
            authorName = request.user.first_name + " " + request.user.last_name
        if title == '':
            return render(request, 'shareresource.html', {'error': "Title is not given"})
        else:
            title = request.POST['blog_title']
        if pubDateTime == '':
            pubDateTime = timezone.now()
        if description == '':
            return render(request, 'shareresource.html', {'error': "Description is not written"})
        else:
            description = request.POST['description']
        if imageFirst == '':
            return render(request, 'shareresource.html', {'error': "Image first is not given"})
        else:
            imageFirst = request.POST['image_first']
        if imageSecond == '':
            return render(request, 'shareresource.html', {'error': "Image Two is not given"})
        else:
            imageSecond = request.POST['image_second']
        if blogCategory == '':
            return render(request, 'shareresource.html', {'error': "Blog Category is not selected"})
        else:
            blogCategory = request.POST['blog_category']
        if refrenceLinks == '':
            return render(request, 'shareresource.html', {'error': "Refrence links not given"})
        else:
            refrenceLinks = request.POST['refrence_link']
        blogsInfo = BlogsInfo(title=title, pubDateTime=pubDateTime, description=description, imageSecond=imageSecond, imageFirst=imageFirst,
                              UserType=UserType, authorName=authorName, blogCategory=blogCategory, refrenceLinks=refrenceLinks, us_id=request.user.id)
        blogsInfo.save()
        print("author name:" + authorName)
        return render(request, 'blog_write.html', {'error': "Successfully added the blog!"})


def shareResource(request):
    event = OrganiseEvent.objects.filter(us_id=request.user.id)
    return render(request, 'shareresource.html', {'event': event})


def editResource(request):
    share_resource = ShareResource.objects.filter(us=request.user.id)
    return render(request, 'edit_shareresource.html', {'share_resource': share_resource})


def updateShareResources(request, id):
    share = ShareResource.objects.get(pk=id)
    if request.method == 'POST':

        submitbutton = request.POST.get('Submit')
        if submitbutton:
            share_resource = ShareResource.objects.get(pk=id)
            event_title = request.POST['event_name']
            subject = request.POST['subject']
            description = request.POST['description']
            publishedDate = timezone.now()
            resourceLink = request.POST['addlinks']
            documentFile = request.POST['document_file']
            publisedBy = request.POST['published_by']
            resourceImage = request.POST['share_image']
            if documentFile == '':
                resourceImage = share_resource.resourceImage
            else:
                resourceImage = request.POST['share_image']
            if resourceImage == '':
                documentFile = share_resource.documentFile
            else:
                documentFile = request.POST['document_file']

 
            userr = User.objects.get(pk= request.user.id)
          
            orgid = OrganiseEvent.objects.get(id=share.org_id.id)
            # print("org id",orgid)

            share_resource = ShareResource(id=share_resource.id, event_title=event_title, subject=subject, description=description, publishedDate=publishedDate,
                                           resourceLink=resourceLink, documentFile=documentFile, publisedBy=publisedBy, resourceImage=resourceImage, us=userr,org_id=orgid )
            share_resource.save()
            share_resource.refresh_from_db()
            share_resource = ShareResource.objects.filter(
                us_id=request.user.id)
            return render(request, 'edit_shareresource.html', {'share_resource': share_resource})


def resource(request):
    if request.method == 'POST':
        event_title = request.POST['event_name']
        subject = request.POST['subject']
        description = request.POST['descr']
        publishedDate = request.POST['published_date']
        resourceLink = request.POST['addlinks']
        documentFile = request.POST['document_file']
        publisedBy = request.POST['published_by']
        resourceImage = request.POST['share_image']
        if event_title == '':
            return render(request, 'shareresource.html', {'error': "Event is not selected"})
        else:
            event_title = request.POST['event_name']
        if subject == '':
            return render(request, 'shareresource.html', {'error': "Event is not selected"})
        else:
            subject = request.POST['subject']
        if description == '':
            return render(request, 'shareresource.html', {'error': "Event is not selected"})
        else:
            description = request.POST['descr']
        if publishedDate == '':
            return render(request, 'shareresource.html', {'error': "Event is not selected"})
        else:
            publishedDate = request.POST['published_date']
        if resourceLink == '':
            return render(request, 'shareresource.html', {'error': "Event is not selected"})
        else:
            resourceLink = request.POST['addlinks']
        if documentFile == '':
            return render(request, 'shareresource.html', {'error': "Event is not selected"})
        else:
            documentFile = request.POST['document_file']
        if publisedBy == '':
            return render(request, 'shareresource.html', {'error': "Event is not selected"})
        else:
            publisedBy = request.POST['published_by']
        if resourceImage == '':
            return render(request, 'shareresource.html', {'error': "Event is not selected"})
        else:
            resourceImage = request.POST['share_image']

        orgid = OrganiseEvent.objects.get(event_title=event_title)

        share_resource = ShareResource(event_title=event_title, subject=subject, description=description, publishedDate=publishedDate, resourceLink=resourceLink,
                                       documentFile=documentFile, publisedBy=publisedBy, resourceImage=resourceImage, us_id=request.user.id, org_id=orgid)
        share_resource.save()

        share_resource = ShareResource.objects.filter(us_id=request.user.id)

        return render(request, 'shareresource.html', {'share_resource': share_resource})


def evenDetailsUpdate(request, id):
    if request.method == 'POST':
        events = EventDetails.objects.get(pk=id)
        event = request.POST['event_title']
        no_participant = request.POST['no_participant']
        expected_participant = request.POST['expected_participant']
        event_level = request.POST['event_level']
        eligibility = request.POST['eligibility']
        prerequisite = request.POST['prerequisite']
        facility = request.POST['facilities']
        event_detail_docs = request.POST['event_detail_docs']
        submitbutton = request.POST.get('Submit')
        if submitbutton:
            if event_detail_docs == '':

                event_detail_docs = events.event_detail_docs
                userr = User.objects.get(pk= request.user.id)
                # print("orggg id",events.org_id.id)
                # print("ehj",events.id)
                orgid = OrganiseEvent.objects.get(id=events.org_id.id)
                # print("org id",orgid)

                eventInstance = EventDetails(id=id, event=event, no_participant=no_participant, expected_participant=expected_participant, event_level=event_level,
                                             eligibility=eligibility, prerequisite=prerequisite, facility=facility, event_detail_docs=event_detail_docs, us=userr,org_id= orgid)
                eventInstance.save()
                return render(request, 'addrubrics.html', {'registered': 'Event Successfully Registered!'})
        else:
            if event == '':
                return render(request, 'update_rubrics.html', {'registered': 'Event Successfully Registered!'})
            else:
                event = request.POST['event_name']
            if no_participant == '':
                return render(request, 'update_rubrics.html', {'registered': 'Event Successfully Registered!'})
            else:
                no_participant = request.POST['no_participant']
            if expected_participant == '':
                return render(request, 'update_rubrics.html', {'registered': 'Event Successfully Registered!'})
            else:
                expected_participant = request.POST['expected_participant']
            if event_level == '':
                return render(request, 'update_rubrics.html', {'registered': 'Event Successfully Registered!'})
            else:
                event_level = request.POST['event_level']

            if eligibility == '':
                return render(request, 'update_rubrics.html', {'registered': 'Event Successfully Registered!'})
            else:
                eligibility = request.POST['eligibility']
            if prerequisite == '':
                return render(request, 'update_rubrics.html', {'registered': 'Event Successfully Registered!'})
            else:
                prerequisite = request.POST['prerequisite']
            if facility == '':
                return render(request, 'update_rubrics.html', {'registered': 'Event Successfully Registered!'})
            else:
                facility = request.POST['facilities']
            if event_detail_docs == '':

                return render(request, 'update_rubrics.html', {'registered': 'Event Successfully Registered!'})
            else:
                event_detail_docs = request.POST['event_detail_docs']


def returnEditRubrics(request):
    events = EventDetails.objects.filter(us=request.user.id)
    return render(request, 'update_rubrics.html', {'events': events})


def eventUpdate(request, id):
    if request.method == 'POST':
        submitbutton = request.POST.get('Submit')
        if submitbutton:
            eventid = OrganiseEvent.objects.get(pk=id)
            # print('get the id ', eventid.id)
            userl = User.objects.get(pk=request.user.id)
            # print("user id is ",userl)
            event_title = request.POST['event_title']
            event_description = request.POST['event_description']
            event_category = request.POST['event_category']
            org_name = request.POST['org_by']
            org_email = request.POST['org_email']
            org_mobile = request.POST['mobile']
            org_contact_person = request.POST['person_name']
            event_poster = request.POST['event_poster']
            event_startdate = request.POST['event_startdate']
            event_enddate = request.POST['event_enddate']
            
            if event_startdate == '':
                event_startdate=eventid.event_startdate  
            else:
                event_startdate = request.POST['event_startdate']
            if event_enddate == '':
                event_enddate =eventid.event_enddate
            else:
                event_enddate = request.POST['event_enddate']
            if event_poster == '':
                event_poster = eventid.event_poster
            else:
                event_poster = request.POST['event_poster']
            if event_title == '':
                return render(request, 'registered_event.html', {'error': "Please Enter Event Title!"})
            else:
                event_title = request.POST['event_title']
            if event_category == '':
                return render(request, 'registered_event.html', {'error': "Please Select Event Category!"})
            else:
                event_category = request.POST['event_category']
            if org_name == '':
                return render(request, 'registered_event.html', {'error': "Please Enter Org Name!"})
            else:
                org_name = request.POST['org_by']
            if org_email == '':
                return render(request, 'registered_event.html', {'error': "Please Enter Org Email!"})
            else:
                org_email = request.POST['org_email']
            if org_mobile == '':
                return render(request, 'registered_event.html', {'error': "Please Enter Org Mobile!"})
            else:
                org_mobile = request.POST['mobile']
            if org_contact_person == '':
                return render(request, 'registered_event.html', {'error': "Please Enter Contact Person Name!"})
            else:
                org_contact_person = request.POST['person_name']

            sve=OrganiseEvent(id=eventid.id,event_title=event_title,event_category= event_category,org_name=org_name,org_email=org_email,org_mobile=org_mobile,org_contact_person=org_contact_person,event_poster=event_poster,event_startdate=event_startdate,event_enddate=event_enddate,us=userl,event_description=event_description)
            sve.save()

            event = OrganiseEvent.objects.filter(us=request.user.id)
            context = {'events': event,'updated':'Successfully updated event '}
            return render(request, 'registered_event.html',context)
        else:
            events = OrganiseEvent.objects.filter(us=request.user.id)
            context = {'events': events}
            return render(request, 'registered_event.html', context)


def eventDetails(request):
    if request.method == 'POST':
        event = request.POST['event_name']
        no_participant = request.POST['no_participant']
        expected_participant = request.POST['expected_participant']
        event_level = request.POST['event_level']
        eligibility = request.POST['eligibility']
        prerequisite = request.POST['prerequisite']
        facility = request.POST['facilities']
        event_detail_docs = request.POST['event_detail_docs']
        if event == '':
            return render(request, 'addrubrics.html', {'error': "Event is not selected"})
        else:
            event = request.POST['event_name']
        if no_participant == '':
            return render(request, 'addrubrics.html', {'error': "No Participant not filled!"})
        else:
            no_participant = request.POST['no_participant']
        if expected_participant == '':
            return render(request, 'addrubrics.html', {'error': "No Participant not filled!"})
        else:
            expected_participant = request.POST['expected_participant']
        if event_level == '':
            return render(request, 'addrubrics.html', {'error': "Event level field not selected"})
        else:
            event_level = request.POST['event_level']
        if eligibility == '':
            return render(request, 'addrubrics.html', {'error': "Eligibility  field not selected"})
        else:
            eligibility = request.POST['eligibility']
        if prerequisite == '':
            return render(request, 'addrubrics.html', {'error': "Prerequisite field not filled"})
        else:
            prerequisite = request.POST['prerequisite']
        if facility == '':
            return render(request, 'addrubrics.html', {'error': "Facility field not filled"})
        else:
            facility = request.POST['facilities']
        if event_detail_docs == '':
            return render(request, 'addrubrics.html', {'error': "File is not attached"})
        else:
            event_detail_docs = request.POST['event_detail_docs']

        orgid = OrganiseEvent.objects.get(event_title=event)

        eventInstance = EventDetails(event=event, no_participant=no_participant, expected_participant=expected_participant, event_level=event_level, eligibility=eligibility, prerequisite=prerequisite,
                                     facility=facility, event_detail_docs=event_detail_docs, us_id=request.user.id, org_id=orgid)

        eventInstance.save()
        eventDetails = EventDetails.objects.filter(us=request.user.id)
        eventsOrganise = OrganiseEvent.objects.filter(us=request.user.id)
        context = {	'eventDetails': eventDetails,
                    'eventsOrganise': eventsOrganise,
                    'registered': 'Event Successfully Registered!'
                    }
        return render(request, 'addrubrics.html', context)


def organiseEventFormData(request):
    if request.method == 'POST':
        event_title = request.POST['event_title']
        event_description = request.POST['event_description']
        event_category = request.POST['event_category']
        org_name = request.POST['org_by']
        org_email = request.POST['org_email']
        org_mobile = request.POST['mobile']
        org_contact_person = request.POST['person_name']
        event_poster = request.POST['event_poster']
        event_startdate = request.POST['event_startdate']
        event_enddate = request.POST['event_enddate']
        if OrganiseEvent.objects.filter(event_title=event_title).exists():
            return render(request, 'organise_event.html', {'error': "Event already Registered!"})
        else:

            if event_title == '':
                return render(request, 'organise_event.html', {'error': "Please Enter Event Title!"})
            else:
                event_title = request.POST['event_title']

            if event_description == '':
                return render(request, 'organise_event.html', {'error': "Please Enter Event Title!"})
            else:
                event_description = request.POST['event_description']

            if event_category == '':
                return render(request, 'organise_event.html', {'error': "Please Select Event Category!"})
            else:
                event_category = request.POST['event_category']

            if org_name == '':
                return render(request, 'organise_event.html', {'error': "Please Enter Org Name!"})
            else:
                org_name = request.POST['org_by']
            if org_email == '':
                return render(request, 'organise_event.html', {'error': "Please Enter Org Email!"})
            else:
                org_email = request.POST['org_email']
            if org_mobile == '':
                return render(request, 'organise_event.html', {'error': "Please Enter Org Mobile!"})
            else:
                org_mobile = request.POST['mobile']
            if org_contact_person == '':
                return render(request, 'organise_event.html', {'error': "Please Enter Contact Person Name!"})
            else:
                org_contact_person = request.POST['person_name']
            if event_poster == '':
                return render(request, 'organise_event.html', {'error': "Please Select Event Poster!"})
            else:
                event_poster = request.POST['event_poster']
            if event_startdate == '':
                return render(request, 'organise_event.html', {'error': "Please  Select Start Date!"})
            else:
                event_startdate = request.POST['event_startdate']
            if event_enddate == '':
                return render(request, 'organise_event.html', {'error': "Please Select End Date !"})
            else:
                event_enddate = request.POST['event_enddate']

            userid = User.objects.get(pk=request.user.id)

            event = OrganiseEvent(event_title=event_title, event_description=event_description, event_category=event_category, org_name=org_name,
                                  org_email=org_email, org_mobile=org_mobile, org_contact_person=org_contact_person,
                                  event_poster=event_poster, event_startdate=event_startdate,
                                  event_enddate=event_enddate, us=userid)
            event.save()
            # return render(request,'organise_event.html',{'event':'Event Successfully Registered!'})
            events = OrganiseEvent.objects.filter(us=request.user.id)
            loc = Event_Location.objects.filter(eventid_id=request.user.id)
            context = {'events': events, 'loc': loc}
            return render(request, 'registered_event.html', context)


def addrubrics(request):
    eventDetails = EventDetails.objects.filter(us=request.user.id)
    eventsOrganise = OrganiseEvent.objects.filter(us=request.user.id)
    context = {	'eventDetails': eventDetails,
                'eventsOrganise': eventsOrganise
                }
    return render(request, 'addrubrics.html', context)


def organiseEvent(request):
    events = OrganiseEvent.objects.filter(us=request.user.id)
    return render(request, 'organise_event.html', {'events': events})


def eventEdit(request, id):
    event = get_object_or_404(OrganiseEvent, pk=id)
    #event =get_object_or_404(EventDetails,pk=id)
    return render(request, 'sponsor_event.html', {'event': event})


def registeredEvent(request):
    events = OrganiseEvent.objects.filter(us=request.user.id)
    loc = Event_Location.objects.filter(eventid_id=request.user.id)
    context = {'events': events, 'loc': loc}
    return render(request, 'registered_event.html', context)


def indx(request):
    return render(request, 'organiser_index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        form.save()
        if form.is_valid():
            print("Validation Success!!")
            print("name :" + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text:" + form.cleaned_data['text'])
    return render(request, 'organiser.html', {'form': form})


def about(request):
    return render(request, 'pages/index.html')


def profile_org(request):
    profile=UserProfile.objects.filter(id=request.user.id)
    return render(request, 'profile_org.html', {'profil':profile})


def editProfile(request):
    profiles = UserProfile.objects
    return render(request, 'editProfile.html', {'profiles': profiles})


def about(request):
    return render(request, 'pages/index.html')


def updateProfile(request):
    if request.method == 'POST':
        submitbutton = request.POST.get('Submit')
        if submitbutton:
            user = request.POST['user']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']

            profiles = User(id=request.user.id, username=user,
                            first_name=fname, last_name=lname, email=email)
            profiles.save()
            profiles.refresh_from_db()
            edit_profile = UserProfile.objects
            return render(request, 'profile.html', {'edit_profile': edit_profile})

def del_profile(request,id):
    profile=User.objects.filter(id=id)
    profile.delete()
    return render(request, 'login.html',{'error':"CREATE A NEW PROFILE NOW"})


def req_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'as_attachment=True; filename="mypdf.pdf"'
    response['Content-Disposition'] = 'inline'
    filename = "mypdf.pdf"

    buffer = io.BytesIO()
    buffer.pagesize = A4
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)


    p.line(80, 770, 480, 770)
    p.drawString(80, 755, 'TECHEVENT USER DETAILS :')
    p.line(80, 750, 480, 750)
    # Start writing the PDF here
    p.drawString(80, 725, 'Email ')
    p.drawString(200, 725, ': ')
    p.drawString(250, 725, request.user.email)
    p.line(80, 700, 480, 700)
    p.drawString(80, 675, 'User Name ')
    p.drawString(200, 675, ': ')
    p.drawString(250, 675, request.user.username)
    p.drawString(80, 650, 'First Name ')
    p.drawString(200, 650, ': ')
    p.drawString(250, 650, request.user.first_name)
    p.drawString(80, 625, 'Last Name ')
    p.drawString(200, 625, ': ')
    p.drawString(250, 625, request.user.last_name)
    p.line(80, 550, 480, 550)
    p.drawString(
        80, 532, 'DATA RETRIVED FROM DATA BASE IF ERROR CONTACT ADMIN')
    p.line(80, 525, 480, 525)
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

