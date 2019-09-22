from django.shortcuts import render, redirect, get_object_or_404
from Organizer.models import OrganiseEvent, EventDetails, ShareResource
from Participant.models import ParticipateEvent, EventFeeback
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.utils import timezone
from Blog.models import BlogsInfo
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
import io


def about(request):
    return render(request, 'participant_index.html')


def participate(request):
    even = EventDetails.objects
    return render(request, 'participant_index.html', {'even': even})


def part_profile(request):
    return render(request, 'part_profile.html', {})


def part_editProfile(request):
    part_profiles = UserProfile.objects
    return render(request, 'part_editProfile.html', {'part_profiles': part_profiles})


def part_updateProfile(request):
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
            edit_profile = UserProfile.filter(us=request.user.id)
            return render(request, 'part_profile.html', {'part_profile': edit_profile})


def deleteparticipant(request):
    User.objects.filter(username=request.user.username).delete()
    #messages.success(request,'Profile have been Successfully deleted')
    return render(request, 'login.html', {'error': 'Profile have been Successfully deleted'})


def event_details(request):
    events = OrganiseEvent.objects
    return render(request, 'event_details.html', {'events': events})


def part_for(request):
    part_event = ParticipateEvent.objects.get(us=request.user.id)
    events = OrganiseEvent.objects.filter(id=part_event.Event_id_id)
    return render(request, 'list_part_events.html', {'events': events})


def participatein_event(request, id):
    part_event = ParticipateEvent.objects.filter(us=request.user.id)
    events = OrganiseEvent.objects.filter(us=request.user.id)
    part_early = ParticipateEvent.objects.filter(
        us_id=request.user.id, Event_id_id=id)
    if part_early is not None:
        try:
            events = OrganiseEvent.objects.get(pk=id)
            eventdet = EventDetails.objects.get(org_id=id)
            print("hello", eventdet)

            context = {	'events': events,
                        'eventdet': eventdet,
                        }

            print("event is", events.event_title)
            return render(request, 'participated_event.html', context)
        except EventDetails.DoesNotExist:
            eventdet = None
            if eventdet:
                pass
            else:
                events = OrganiseEvent.objects.get(pk=id)
                context = {	'events': events,
                            'eventdet': eventdet,
                            }

                print("event is", events.event_title)
                return render(request, 'participated_event.html', context)
    else:
        participated_event = ParticipateEvent(
            Event_id_id=id, us_id=request.user.id)
        participated_event.save()
        participated_event.refresh_from_db()
        try:
            events = OrganiseEvent.objects.get(pk=id)
            eventdet = EventDetails.objects.get(org_id=id)
            print("hello", eventdet)

            context = {	'events': events,
                        'eventdet': eventdet,
                        }

            print("event is", events.event_title)
            return render(request, 'participated_event.html', context)
        except EventDetails.DoesNotExist:
            eventdet = None
            if eventdet:
                pass
            else:
                events = OrganiseEvent.objects.get(pk=id)
                context = {	'events': events,
                            'eventdet': eventdet,
                            }

                print("event is", events.event_title)
                return render(request, 'participated_event.html', context)


def part_shareresources(request, id):
    try:
        resources = ShareResource.objects.get(org_id_id=id)
        return render(request, 'part_shareresources.html', {'resources': resources})
    except ShareResource.DoesNotExist:
        resources = None
    if resources:
        pass
    else:
        return render(request, 'part_shareresources.html', {'error': 'Resources are not published'})


def enquireInfoMail(request):
    if request.POST:
        subject = request.POST['subject']
        to = request.POST['to']
        fromm = request.POST['from']
        mobile = request.POST['mobile']
        message = request.POST['message']
        send_mail('Subject' + subject,
                  'Message' + message + 'Will Contact your soon',
                  'sachin.thakur9614@gmail.com',
                  [to, 'sachin.thakur@mca.christuniversity.in', ],
                  fail_silently=False)

        return render('Participant_index.html')


def enquireInfo(request, id):
    event = OrganiseEvent.objects.get(pk=id)
    usr_det = UserProfile.objects.get(pk=request.user.id)
    return render(request, 'part_enquire.html', {'usr_det': usr_det, 'event': event})


def part_enquire(request):
    usr_det = UserProfile.objects.get(pk=request.user.id)
    return render(request, 'part_enquire.html', {'usr_det': usr_det})


def partblogsDetails(request):
    blogsInfo = BlogsInfo.objects.filter(us=request.user.id)
    return render(request, 'part-blog_edit.html', {'blogsInfo': blogsInfo})


def partblog(request):
    return render(request, 'part-blog_write.html')


def partWriteBlog(request):
    if request.method == 'POST':
        title = request.POST['blog_title']
        pubDateTime = timezone.now()
        description = request.POST['description']
        imageSecond = request.POST['image_second']
        imageFirst = request.POST['image_first']
        blogCategory = request.POST['blog_category']
        refrenceLinks = request.POST['refrence_link']
        UserType = 'Participant'
        if request.user.is_authenticated:
            authorName = request.user.first_name + " " + request.user.last_name
        if title == '':
            return render(request, 'part-blog_write.html', {'error': "Title is not given"})
        else:
            title = request.POST['blog_title']
        if pubDateTime == '':
            pubDateTime = timezone.now()
        if description == '':
            return render(request, 'part-blog_write.html', {'error': "Description is not written"})
        else:
            description = request.POST['description']
        if imageFirst == '':
            return render(request, 'part-blog_write.html', {'error': "Image first is not given"})
        else:
            imageFirst = request.POST['image_first']
        if imageSecond == '':
            return render(request, 'part-blog_write.html', {'error': "Image Two is not given"})
        else:
            imageSecond = request.POST['image_second']
        if blogCategory == '':
            return render(request, 'part-blog_write.html', {'error': "Blog Category is not selected"})
        else:
            blogCategory = request.POST['blog_category']
        if refrenceLinks == '':
            return render(request, 'part-blog_write.html', {'error': "Refrence links not given"})
        else:
            refrenceLinks = request.POST['refrence_link']
        blogsInfo = BlogsInfo(title=title, pubDateTime=pubDateTime, description=description, imageSecond=imageSecond, imageFirst=imageFirst,
                              UserType=UserType, authorName=authorName, blogCategory=blogCategory, refrenceLinks=refrenceLinks, us_id=request.user.id)

        blogsInfo.save()
        print("author name:" + authorName)
        return render(request, 'part-blog_write.html', {'error': "Blog is selected"})


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
    p.drawString(80, 755, 'HACKATHON USER DETAILS :')
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


def part_feedback(request):
    event_id = ParticipateEvent.objects.get(us=request.user.id)
    event = OrganiseEvent.objects.filter(pk=event_id.Event_id_id)
    usr = User.objects.get(pk=request.user.id)
    usr_det = UserProfile.objects.get(pk=request.user.id)
    return render(request, 'part_feedback.html', {'usr': usr, ' usr_det': usr_det, 'event': event})


def feedback_load(request):
    event_id = ParticipateEvent.objects.get(us=request.user.id)
    event = OrganiseEvent.objects.filter(pk=event_id.Event_id_id)
    usr = User.objects.get(pk=request.user.id)
    usr_det = UserProfile.objects.get(pk=request.user.id)
    return render(request, 'part_feedback.html', {'usr': usr, ' usr_det': usr_det, 'event': event, 'event_part': event})


def feedback(request):
    if request.method == 'POST':
        event = OrganiseEvent.objects.filter(us=request.user.id)
        subject = request.POST['subject']
        pubDateTime = timezone.now()
        feedback = request.POST['feedback']
        UserType = 'Participant'
        if subject == '':
            return render(request, 'part_feedback.html', {'error': "Subject is not given"})
        else:
            subject = request.POST['subject']
        if pubDateTime == '':
            pubDateTime = timezone.now()
        if feedback == '':
            return render(request, 'part_feedback.html', {'error': "Feedback is not written"})
        else:
            feedback = request.POST['feedback']
        eventFeeback = EventFeeback(subject=subject, feedback=feedback,
                                    pubDateTime=pubDateTime, Event_id_id=event, us_id=request.user.id)

        eventFeeback.save()
        eventFeeback.refresh_from_db()
        print("author name:" + authorName)
        return render(request, 'part_feedback.html', {'error': "Feedback is stored"})
