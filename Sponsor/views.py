from django.shortcuts import render, get_object_or_404
from Blog.models import BlogsInfo
from Organizer.models import EventDetails, SponsorShip, OrganiseEvent, Event_Location
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from media.paytm import Checksum
from accounts.models import UserProfile
from .models import SponsorTransaction

MERCHANT_KEY = 'P7HtuKq8&zpmzxZE'


def sponsoredEvent(request):
    sponsor = SponsorTransaction.objects.get(us=request.user.id)
    event = OrganiseEvent.objects.get(pk=sponsor.org_id.id)
    return render(request, 'sponsored_event.html', {'sponsor': sponsor, 'event': event})


def transaction(request, id):
    spnsr = SponsorShip.objects.get(pk=id)
    print("Spnsor id is", spnsr.org_id.id)
    userid = User.objects.get(pk=request.user.id)
    orgid = OrganiseEvent.objects.get(pk=spnsr.org_id.id)
    if request.method == 'POST':
        try:
            spnsrtype = 'sponsertype' in request.POST and request.POST['sponsertype']
            amount = 'amount' in request.POST and request.POST['amount']
            # is_private = request.POST['is_private']
            # spnsrtype
            # spnsrtype = request.POST['sponsertype']
            # amount = request.POST['amount']
            try:
                spn = SponsorTransaction.objects.get(org_id=orgid)
                events = OrganiseEvent.objects
                return render(request, 'sponsor_event.html', {'error': 'Already Sponsored ', })
            except SponsorTransaction.DoesNotExist:
                spn = None
                if spn is None:
                    transaction = SponsorTransaction(
                        spnsortype=spnsrtype, amount=amount, org_id=orgid, us=userid)
                    transaction.save()
                    return render(request, 'sponsored_event.html')
                else:
                    events = OrganiseEvent.objects
                    return render(request, 'sponsor_event.html', {'error': 'Already sponsored'})
        except MultiValueDictKeyError:
            spnsrtype = False
            amount = False

            return render(request, 'sponsored_event.html')


def sponsor(request):
    return render(request, 'sponsor_index.html')

# user profile


def profile(request):
    profile = UserProfile.objects.filter(id=request.user.id)
    return render(request, 'profile_spnsr.html', {'profile': profile})


@csrf_exempt
def handleRequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print("successful")
            return render(request, 'paymentstatus.html', {'respon': response_dict})

        else:
            print('not successful'+response_dict['RESPMSG'])
            return render(request, 'paymentstatus.html', {'response': response_dict})


@csrf_exempt
def payAmount(request):
    # amount=10
    if request.method == 'POST':

        idd = request.POST.get('sp', False)

        # idd = request.POST['sp']
        print("id is", idd)

        spnr = SponsorShip.objects.get(pk=idd)

        print("SponsorShip", spnr.ex_platinum)

    param_dict = {
        "MID": "bClJNU50572288826034",
        "ORDER_ID": str(7),
        "CUST_ID": str(7),
        "TXN_AMOUNT": str(spnr.ex_platinum),
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        'CALLBACK_URL': 'http://127.0.0.1:8000/Sponsor/amount/' + str(spnr.id)}

    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(
        param_dict, MERCHANT_KEY)

    return render(request, 'payment_paytm.html', {'param_dict': param_dict})


@csrf_exempt
def amount(request, id):

    return render(request, 'payment_paytm.html')


def payment(request):

    param_dict = {
        "MID": "bClJNU50572288826034",
        "ORDER_ID": str(request.user.id),
        "CUST_ID": str(3),
        "TXN_AMOUNT": str(amt),
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        'CALLBACK_URL': 'http://127.0.0.1:8000/Sponsor/payAmount/'}

    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(
        param_dict, MERCHANT_KEY)


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
# @csrf_exempt


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


def blogDetailSponsor(request):
    blogsInfo = BlogsInfo.objects.filter(us=request.user.id)
    return render(request, 'blog_edit-sponsor.html', {'blogsInfo': blogsInfo})

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
                              UserType=UserType, authorName=authorName, blogCategory=blogCategory, refrenceLinks=refrenceLinks, us_id=request.user.id)
        blogsInfo.save()
        print("author name:" + authorName)
        return render(request, 'blog_write_sponsor.html', {'error': title + "Blog is written"})
