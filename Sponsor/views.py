from django.shortcuts import render, get_object_or_404
from Blog.models import BlogsInfo
from Organizer.models import EventDetails, SponsorShip, OrganiseEvent, Event_Location
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail

# index


def sponsor(request):
    return render(request, 'sponsor_index.html')

# user profile


def profile(request):
    profile = User.objects.filter(id=request.user.id)
    return render(request, 'profile_spnsr.html', {'profile': profile})

# to contact event organisers


def enquireInfoMail(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        to = request.POST.get('to')
        fromm = request.POST.get('from')
        mobile = request.POST['mobile']
        message = request.POST['message']
        send_mail('Subject' + subject,
                  'Message' + message + 'Will Contact your soon',
                  'sachin.thakur9614@gmail.com',
                  [to, 'sachin.thakur@mca.christuniversity.in', ],
                  fail_silently=False)

        return render(request, 'sponsor_enquire.html', {'send': "MAIL SEND SUCCESSFULLY !"})
    else:
        events = OrganiseEvent.objects
        return render(request, 'sponsor_enquire.html', {'event': events})

# list out events to sponser


def sponsor_event(request):
    try:
        events = OrganiseEvent.objects
        return render(request, 'sponsor_event.html', {'event': events})
    except:
        return render(request, 'sponsor_event.html')

# list out sponsership details of events to sponser


def addsponsershipinfo(request):
    if request.method == 'POST':
        event = request.POST['event_name']
        spnsr_det = SponsorShip.objects.filter(event_title=event)
        events = OrganiseEvent.objects
        return render(request, 'sponsor_event.html', {'event': events, 'spnsr_details': spnsr_det})
    else:
        events = OrganiseEvent.objects
        return render(request, 'sponsor_event.html', {'event': events})

# save the sponsership info to db


def addsponsership(request):
    events = OrganiseEvent.objects
    return render(request, 'sponsor_event.html', {'event': events})

# list out all event info


def events(request):
    events = OrganiseEvent.objects
    return render(request, 'sponsor_up_coming.html', {'events': events})

# load more event info


def event_details(request, id):
    if(OrganiseEvent.objects.filter(id=id) is not None):
        events = OrganiseEvent.objects.filter(id=id)
        if(EventDetails.objects.filter(id=id) is not None):
            info_event = EventDetails.objects.filter(id=id)
            if(SponsorShip.objects.filter(id=id) is not None):
                spnsr_info = SponsorShip.objects.filter(id=id)
                if(Event_Location.objects.filter(id=id) is not None):
                    loc = Event_Location.objects.filter(id=id)
                    return render(request, 'sponsor_event_details.html', {'events': events, 'info': info_event, 'spnsr': spnsr_info, 'venue': loc})
                else:
                    return render(request, 'sponsor_event_details.html', {'events': events, 'info': info_event, 'spnsr': spnsr_info})
            else:
                return render(request, 'sponsor_event_details.html', {'events': events, 'info': info_event})
        else:
            return render(request, 'sponsor_event_details.html', {'events': events})
    else:
        events = OrganiseEvent.objects
        return render(request, 'sponsor_up_coming.html', {'events': events})

# list out sponsered events


def sponsoredEvent(request):
    sponsors = SponsorShip.objects
    event = EventDetails.objects
    return render(request, 'sponsored_event.html', {'sponsors': sponsors, 'event': event})

# enquire load


def enquire(request):
    events = OrganiseEvent.objects
    return render(request, 'sponsor_enquire.html', {'event': events})

# setting to address to enquire


def enquire_event(request):
    if request.POST:
        eve = request.POST['event_name']
        if eve == " ":
            events = OrganiseEvent.objects
            return render(request, 'sponsor_enquire.html', {'event': events})
        else:
            events = OrganiseEvent.objects
            even = OrganiseEvent.objects.get(event_title=eve)
            return render(request, 'sponsor_enquire.html', {'event': events, 'evet': even})
    else:
        events = OrganiseEvent.objects
        return render(request, 'sponsor_enquire.html', {'event': events})

# blog load


def blogSponsor(request):
    return render(request, 'blog_write_sponsor.html')

# blog to database


def writeBlogSponsor(request):
    if request.method == 'POST':
        title = request.POST['blog_title']
        pubDateTime = timezone.now()
        description = request.POST['description']
        imageSecond = request.POST['image_second']
        imageFirst = request.POST['image_first']
        blogCategory = request.POST['blog_category']
        refrenceLinks = request.POST['refrence_link']
        UserType = 'Sponsor'
        if request.user.is_authenticated:
            authorName = request.user.first_name + " " + request.user.last_name
        if title == '':
            return render(request, 'blog_write_sponsor.html', {'error': "Title is not given"})
        else:
            title = request.POST['blog_title']
        if pubDateTime == '':
            pubDateTime = timezone.now()
        if description == '':
            return render(request, 'blog_write_sponsor.html', {'error': "Description is not written"})
        else:
            description = request.POST['description']
        if imageFirst == '':
            return render(request, 'blog_write_sponsor.html', {'error': "Image first is not given"})
        else:
            imageFirst = request.POST['image_first']
        if imageSecond == '':
            return render(request, 'blog_write_sponsor.html', {'error': "Image Two is not given"})
        else:
            imageSecond = request.POST['image_second']
        if blogCategory == '':
            return render(request, 'blog_write_sponsor.html', {'error': "Blog Category is not selected"})
        else:
            blogCategory = request.POST['blog_category']
        if refrenceLinks == '':
            return render(request, 'blog_write_sponsor.html', {'error': "Refrence links not given"})
        else:
            refrenceLinks = request.POST['refrence_link']
        blogsInfo = BlogsInfo(title=title, pubDateTime=pubDateTime, description=description, imageSecond=imageSecond, imageFirst=imageFirst,
                              UserType=UserType, authorName=authorName, blogCategory=blogCategory, refrenceLinks=refrenceLinks)
        blogsInfo.save()
        print("author name:" + authorName)
        return render(request, 'blog_write_sponsor.html', {'error': "Event is not selected"})
