from django.shortcuts import render,get_object_or_404
from Blog.models import BlogsInfo
from Organizer.models import EventDetails,SponsorShip,EventDetails,OrganiseEvent
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail  import send_mail


def sponsor(request):
	return  render(request,'sponsor_index.html')


def enquireInfoMail(request):
	if request.method=='POST':
		subject = request.POST['subject']
		to = request.POST.get('to')
		fromm = request.POST.get('from')
		mobile = request.POST['mobile']
		message = request.POST['message']
		send_mail('Subject' +subject,
			'Message'+ message + 'Will Contact your soon',
			'sachin.thakur9614@gmail.com',
			[to,'sachin.thakur@mca.christuniversity.in',],
			fail_silently =False)
		
		return  render(request,'sponsor_enquire.html',{'send':"MAIL SEND SUCCESSFULLY !"})
	else:
		events=OrganiseEvent.objects
		return  render(request,'sponsor_enquire.html',{'event':events})


def sponsorEventDet(request,id):
	eventdet = EventDetails.objects.filter(org_id=id)

	sponsors = SponsorShip.objects
	print(eventdet.event)

	event = EventDetails.objects
	return render(request,'sponsor_event.html',{'sponsors':sponsors,'event':event,'eventdet':eventdet})


def sponsoredEvent(request):
	sponsors = SponsorShip.objects

	event = EventDetails.objects
	return render(request,'sponsor_event.html',{'sponsors':sponsors,'event':event})

def eventInfo(request,id):
	
	events = OrganiseEvent.objects.get(pk=id)
	sponsor  = SponsorShip.objects.get(org_id = id)

	eventdet = EventDetails.objects.get(org_id=id)
	print("hello",eventdet)

	context ={	'events':events,
				'eventdet':eventdet,
				'sponsor':sponsor
			}

	print("event is",events.event_title)
	return render(request,'sponsor_event_details.html',context)




def sponsorUpComing(request):
	sponsors = SponsorShip.objects
	event = OrganiseEvent.objects.all()
	print("event is")
	context ={	'sponsors ':sponsors,
				'event':event,
			}
	return render(request,'sponsor_up_coming.html',context)



def sponsorEventUpdate(request):
	# sponsors =get_object_or_404(SponsorShip,pk=id)
	return render(request,'sponsor_event.html')



def sponsorEventDetails(request,id):
	event = get_object_or_404(EventDetails, pk=id)
	return render(request,'sponsor_event.html')

def enquireInfo(request,id):
	event = OrganiseEvent.objects.get(pk=id)
	return render(request,'sponsor_enquire.html',{'event':event})

def enquire(request):
	events=OrganiseEvent.objects
	return  render(request,'sponsor_enquire.html',{'event':events})

def enquire_event(request):
	if request.POST:
		eve=request.POST['event_name']
		if eve == " ":
			events=OrganiseEvent.objects
			return  render(request,'sponsor_enquire.html',{'event':events})
		else:
			events=OrganiseEvent.objects
			even=OrganiseEvent.objects.get(event_title=eve)
			# print(even.org_email)
			return render(request,'sponsor_enquire.html',{'event':events,'evet':even})
	else:
		events=OrganiseEvent.objects
		return  render(request,'sponsor_enquire.html',{'event':events})

def blogSponsor(request):
	 return render(request,'blog_write_sponsor.html')

def profile(request):
    profile=User.objects.filter(id=request.user.id)
    return render(request, 'profile_spnsr.html', {'profile':profile})

def writeBlogSponsor(request):
	if request.method =='POST':
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
		if title =='':
			return render(request,'blog_write_sponsor.html', {'error':"Title is not given"})	
		else:
			title = request.POST['blog_title']		
		if pubDateTime =='':			
			pubDateTime = timezone.now()
		if description=='':
			return render(request,'blog_write_sponsor.html', {'error':"Description is not written"})	
		else:
			description = request.POST['description']		
		if imageFirst=='':
			return render(request,'blog_write_sponsor.html', {'error':"Image first is not given"})	
		else:
			imageFirst = request.POST['image_first']			
		if imageSecond=='':
			return render(request,'blog_write_sponsor.html', {'error':"Image Two is not given"})	
		else:
			imageSecond = request.POST['image_second']	
		if blogCategory=='':
			return render(request,'blog_write_sponsor.html', {'error':"Blog Category is not selected"})	
		else:
			blogCategory = request.POST['blog_category']		
		if refrenceLinks=='':
			return render(request,'blog_write_sponsor.html', {'error':"Refrence links not given"})	
		else:
			refrenceLinks = request.POST['refrence_link']
		blogsInfo=BlogsInfo(title=title,pubDateTime=pubDateTime,description=description,imageSecond=imageSecond,imageFirst=imageFirst,
			UserType=UserType,authorName=authorName,blogCategory=blogCategory,refrenceLinks=refrenceLinks)
		blogsInfo.save()
		print("author name:" + authorName)
		return render(request,'blog_write_sponsor.html', {'error':"Event is not selected"})	

