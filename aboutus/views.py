from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import AboutDescription
from .models import Contact
from .models import TeamInfo
from .models import OurServices

def addAboutSection(request):
    aboutDesc = AboutDescription.objects
    teaminfo = TeamInfo.objects
    services = OurServices.objects
    return render(request, 'about.html', {'aboutDesc': aboutDesc, 'teaminfo': teaminfo, 'services': services})

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['mobile']
        message = request.POST['message']
        contact = Contact(name=name, email=email,
                          subject=subject, phone=phone, message=message)
        contact.save()
        # send Email
        send_mail('Subject' + subject,
                  'Message' + message + 'Will Contact your soon',
                  'sachin.thakur9614@gmail.com',
                  [email, 'sachin.thakur@mca.christuniversity.in', ],
                  fail_silently=False
                  )
        messages.success(
            request, 'Your request has been submited, We will contact you shortly')
        return mail.send()
