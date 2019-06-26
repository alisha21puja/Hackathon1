from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . import forms
from .models import OrganiseEvent,EventDetails,ShareResource,SponsorShip,SponsorShipDetails
from django.contrib.auth.models import User
from Blog.models import BlogsInfo
from django.utils import timezone









def editSponsorShip(request):
	sponsorShip=SponsorShip.objects
	return render(request,'edit_sponsorship.html',{'sponsorShip':sponsorShip})

def deletesponsor(request,id):
	sponsorShip=SponsorShip.objects.get(id = id)
	sponsorShip.delete();
	sponsorShip=SponsorShip.objects
	return render(request,'edit_sponsorship.html',{'sponsorShip':sponsorShip})
def updateSponsorInfo(request,id):

	submitbutton = request.POST.get('Submit')
	if submitbutton :
		sponsor=SponsorShip.objects.get(pk=id)
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

		sponsor_ship= SponsorShip(id=id,event_title=event_title,platinum_sponsor=platinum_sponsor,f_platinum=f_platinum,ex_platinum=ex_platinum,gold_sponsor=gold_sponsor,
		f_gold=f_gold,ex_gold=ex_gold,silver_sponsor=silver_sponsor,f_silver=f_silver,ex_silver=ex_silver)
		sponsor_ship.save()
		sponsorShip=SponsorShip.objects
		return render(request,'edit_sponsorship.html',{'sponsorShip':sponsorShip})
	else:
		if platinum_sponsor=='':
			return render(request,'edit_sponsorship.html', {'error':"Title is not given"})	
		else:
			platinum_sponsor = request.POST['platinum_sponsor']		
		if f_platinum=='':
			return render(request,'edit_sponsorship.html', {'error':"Title is not given"})	
		else:
			f_platinum == request.POST['f_platinum']		
		if ex_platinum=='':
			return render(request,'edit_sponsorship.html', {'error':"Title is not given"})	
		else:
			ex_platinum = request.POST['ex_platinum']		
		if gold_sponsor=='':
			return render(request,'edit_sponsorship.html', {'error':"Title is not given"})	
		else:
			gold_sponsor = request.POST['gold_sponsor']		
		if f_gold=='':
			return render(request,'edit_sponsorship.html', {'error':"Title is not given"})	
		else:
			f_gold = request.POST['f_gold']		
		if ex_gold=='':
			return render(request,'edit_sponsorship.html', {'error':"Title is not given"})	
		else:
			ex_gold = request.POST['ex_gold']		
		if silver_sponsor=='':
			return render(request,'edit_sponsorship.html', {'error':"Title is not given"})	
		else:
			silver_sponsor = request.POST['silver_sponsor']		
		if f_silver=='':			
			return render(request,'edit_sponsorship.html', {'error':"Title is not given"})	
		else:
			f_silver = request.POST['f_silver'] 		
		if ex_silver=='':
			return render(request,'edit_sponsorship.html', {'error':"Title is not given"})	
		else:
			ex_silver = request.POST['ex_silver']
		

def sponsorShip(request):
	event = OrganiseEvent.objects
	return render(request,'sponsorShip.html',{'event':event})

def sponsorShipDetails(request): 
	if request.method =='POST':
		eventDetail =EventDetails.objects
		event=request.POST['event_title']
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

		if platinum_sponsor=='':
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			platinum_sponsor = request.POST['platinum_sponsor']		
		if f_platinum=='':
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			f_platinum == request.POST['f_platinum']		
		if ex_platinum=='':
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			ex_platinum = request.POST['ex_platinum']		
		if gold_sponsor=='':
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			gold_sponsor = request.POST['gold_sponsor']		
		if f_gold=='':
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			f_gold = request.POST['f_gold']		
		if ex_gold=='':
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			ex_gold = request.POST['ex_gold']		
		if silver_sponsor=='':
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			silver_sponsor = request.POST['silver_sponsor']		
		if f_silver=='':			
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			f_silver = request.POST['f_silver'] 		
		if ex_silver=='':
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			ex_silver = request.POST['ex_silver']
		sponsor_ship= SponsorShip(event_title=event,platinum_sponsor=platinum_sponsor,f_platinum=f_platinum,ex_platinum=ex_platinum,gold_sponsor=gold_sponsor,
			f_gold=f_gold,ex_gold=ex_gold,silver_sponsor=silver_sponsor,f_silver=f_silver,ex_silver=ex_silver)
		sponsor_ship.save()
		return render(request,'sponsorShip.html')
def blogsDetails(request):
	blogsInfo=BlogsInfo.objects
	return render(request,'blog_edit.html',{'blogsInfo':blogsInfo})
def blog(request):
	blogsInfo=BlogsInfo.objects
	return render(request,'blog_write.html',{'blogsInfo':blogsInfo})
def writeBlogs(request):
	if request.method =='POST':	
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
		if title =='':
			return render(request,'shareresource.html', {'error':"Title is not given"})	
		else:
			title = request.POST['blog_title']		
		if pubDateTime =='':
			pubDateTime = timezone.now()
		if description=='':
			return render(request,'shareresource.html', {'error':"Description is not written"})	
		else:
			description = request.POST['description']		
		if imageFirst=='':
			return render(request,'shareresource.html', {'error':"Image first is not given"})	
		else:
			imageFirst = request.POST['image_first']		
		if imageSecond=='':
			return render(request,'shareresource.html', {'error':"Image Two is not given"})	
		else:
			imageSecond = request.POST['image_second']		
		if blogCategory=='':
			return render(request,'shareresource.html', {'error':"Blog Category is not selected"})	
		else:
			blogCategory = request.POST['blog_category']		
		if refrenceLinks=='':
			return render(request,'shareresource.html', {'error':"Refrence links not given"})	
		else:
			refrenceLinks = request.POST['refrence_link']
		blogsInfo=BlogsInfo(title=title,pubDateTime=pubDateTime,description=description,imageSecond=imageSecond,imageFirst=imageFirst,
			UserType=UserType,authorName=authorName,blogCategory=blogCategory,refrenceLinks=refrenceLinks)
		blogsInfo.save()
		print("author name:" + authorName)
		return render(request,'blog_write.html', {'error':"Event is not selected"})	
def shareResource(request):
	event = OrganiseEvent.objects
	return render(request,'shareresource.html',{'event':event})
def editResource(request):
	share_resource=ShareResource.objects	
	return render(request,'edit_shareresource.html',{'share_resource':share_resource})
def updateShareResources(request,id):
	if request.method=='POST':	
		submitbutton = request.POST.get('Submit')
		if submitbutton :
			share_resource=ShareResource.objects.get(pk=id)
			event_title = request.POST['event_name']	
			subject =  request.POST['subject']
			description =  request.POST['description']
			publishedDate= timezone.now()
			resourceLink =  request.POST['addlinks']
			documentFile =  request.POST['document_file']
			publisedBy = request.POST['published_by']
			resourceImage =  request.POST['share_image']
			if documentFile=='':
				resourceImage = share_resource.resourceImage
			else:
				resourceImage =  request.POST['share_image']
			if resourceImage=='':
				documentFile=share_resource.documentFile
			else:
				documentFile =  request.POST['document_file']				
			share_resource=ShareResource(id=id,event_title=event_title,subject=subject,description=description,publishedDate=publishedDate,resourceLink=resourceLink,documentFile=documentFile,publisedBy=publisedBy,resourceImage=resourceImage)
			share_resource.save()
			share_resource.refresh_from_db()		
			share_resource=ShareResource.objects
			return render(request,'edit_shareresource.html',{'share_resource':share_resource})


def resource(request):
	if request.method=='POST':
		event_title = request.POST['event_name']	
		subject =  request.POST['subject']
		description =  request.POST['description']
		publishedDate= request.POST['published_date']
		resourceLink =  request.POST['addlinks']
		documentFile =  request.POST['document_file']
		publisedBy = request.POST['published_by']
		resourceImage =  request.POST['share_image']
		if event_title == '':
			return render(request,'shareresource.html', {'error':"Event is not selected"})	
		else :
			event_title = request.POST['event_name']		
		if subject == '':
			return render(request,'shareresource.html', {'error':"Event is not selected"})	
		else:
			subject =  request.POST['subject']
		if description == '':
			return render(request,'shareresource.html', {'error':"Event is not selected"})	
		else:
			description =  request.POST['description']		
		if publishedDate == '':
			return render(request,'shareresource.html', {'error':"Event is not selected"})	
		else:
			publishedDate= request.POST['published_date']
		if resourceLink == '':
			return render(request,'shareresource.html', {'error':"Event is not selected"})	
		else:
			resourceLink =  request.POST['addlinks']	
		if documentFile == '':
			return render(request,'shareresource.html', {'error':"Event is not selected"})	
		else:
			documentFile =  request.POST['document_file']		
		if publisedBy =='':
			return render(request,'shareresource.html', {'error':"Event is not selected"})	
		else:
			publisedBy = request.POST['published_by']		
		if resourceImage == '':
			return render(request,'shareresource.html', {'error':"Event is not selected"})	
		else:
			resourceImage =  request.POST['share_image']
		share_resource=ShareResource(event_title=event_title,subject=subject,description=description,publishedDate=publishedDate,resourceLink=resourceLink,documentFile=documentFile,publisedBy=publisedBy,resourceImage=resourceImage)
		share_resource.save()
		return render(request,'shareresource.html')







def evenDetailsUpdate(request,id):
	if request.method=='POST':
		events=EventDetails.objects.get(pk=id)
		event = request.POST['event_title']
		no_participant = request.POST['no_participant']
		expected_participant = request.POST['expected_participant']
		event_level = request.POST['event_level']
		eligibility = request.POST['eligibility']
		prerequisite = request.POST['prerequisite']
		facility = request.POST['facilities']
		event_detail_docs = request.POST['event_detail_docs']
		submitbutton = request.POST.get('Submit')
		if submitbutton :
			if event_detail_docs=='':
				event_detail_docs  = events.event_detail_docs
				eventInstance = EventDetails(id=id,event=event,no_participant=no_participant,expected_participant=expected_participant,event_level=event_level,eligibility=eligibility,prerequisite=prerequisite,facility=facility,event_detail_docs=event_detail_docs)
				eventInstance.save()
				return render(request,'addrubrics.html',{'registered':'Event Successfully Registered!'})
		else:

			if event =='':
				return render(request,'update_rubrics.html',{'registered':'Event Successfully Registered!'})
			else:
				event = request.POST['event_name']
			if no_participant =='':
				return render(request,'update_rubrics.html',{'registered':'Event Successfully Registered!'})
			else:
				no_participant= request.POST['no_participant']
			if expected_participant=='':
				return render(request,'update_rubrics.html',{'registered':'Event Successfully Registered!'})
			else:
				expected_participant = request.POST['expected_participant']
			if event_level=='':
				return render(request,'update_rubrics.html',{'registered':'Event Successfully Registered!'})
			else:
				event_level= request.POST['event_level']

			if 	eligibility=='':
				return render(request,'update_rubrics.html',{'registered':'Event Successfully Registered!'})
			else:
				eligibility= request.POST['eligibility']
			if prerequisite=='':
				return render(request,'update_rubrics.html',{'registered':'Event Successfully Registered!'})
			else:
				prerequisite= request.POST['prerequisite']
			if facility=='':
				return render(request,'update_rubrics.html',{'registered':'Event Successfully Registered!'})
			else:
				facility= request.POST['facilities']
			if event_detail_docs=='':

				return render(request,'update_rubrics.html',{'registered':'Event Successfully Registered!'})
			else:
				event_detail_docs=request.POST['event_detail_docs']
def returnEditRubrics(request):
	events=EventDetails.objects
	return render(request,'update_rubrics.html',{'events':events})

def eventUpdate(request,id):
	if request.method=='POST':
		submitbutton= request.POST.get('Submit')
		if submitbutton :
			eventid=OrganiseEvent.objects.get(pk=id)
			event_title = request.POST['event_title']
			event_description  = request.POST['event_description']
			event_category = request.POST['event_category']
			org_name = request.POST['org_by']
			org_email = request.POST['org_email']
			org_mobile = request.POST['mobile']
			org_contact_person = request.POST['person_name']
			event_poster = request.POST['event_poster']
			event_startdate = request.POST['event_startdate']
			event_enddate = request.POST['event_enddate']
			if event_startdate=='':
				event_startdate= eventid.event_startdate;	
			else:
				event_startdate = request.POST['event_startdate']
			if event_enddate=='':
				event_enddate = eventid.event_enddate;
				return render(request,'registered_event.html', {'error':"Please Select End Date !"})				
			else:
				event_enddate = request.POST['event_enddate']
			eve=OrganiseEvent(id=id,event_title = event_title,event_description=event_description,event_category=event_category,org_name=org_name,
									org_email=org_email,org_mobile=org_mobile,org_contact_person=org_contact_person,
									event_poster=event_poster,event_startdate=event_startdate,event_enddate = event_enddate) 
			eve.save()
			
			return render(request,'registered_event.html'	)
		else:			
			if event_title=='':
				return render(request,'registered_event.html', {'error':"Please Enter Event Title!"})	
			else :
				event_title = request.POST['event_title']
			if event_category=='':	
				return render(request,'registered_event.html', {'error':"Please Select Event Category!"})			
			else: 
				event_category = request.POST['event_category']
			if org_name=='':
				return render(request,'registered_event.html', {'error':"Please Enter Org Name!"})				
			else:
				org_name = request.POST['org_by']
			if org_email=='':
				return render(request,'registered_event.html', {'error':"Please Enter Org Email!"})				
			else:
				org_email = request.POST['org_email']
			if org_mobile=='':
				return render(request,'registered_event.html', {'error':"Please Enter Org Mobile!"})
			else :
				org_mobile = request.POST['mobile']
			if org_contact_person=='':
				return render(request,'registered_event.html', {'error':"Please Enter Contact Person Name!"})					
			else:
				org_contact_person = request.POST['person_name']
			if event_poster=='':
				return render(request,'registered_event.html', {'error':"Please Select Event Poster!"})				
			else:
				event_poster = request.POST['event_poster']				
			if event_startdate=='':
				return render(request,'registered_event.html', {'error':"Please  Select Start Date!"})				
			else:
				event_startdate = request.POST['event_startdate']
			if event_enddate=='':
				return render(request,'registered_event.html', {'error':"Please Select End Date !"})				
			else:
				event_enddate = request.POST['event_enddate']

def eventDetails(request):
	#print("Dude ints nnot working")
	if request.method=='POST':
		event = request.POST['event_name']
		no_participant= request.POST['no_participant']
		expected_participant = request.POST['expected_participant']
		event_level= request.POST['event_level']
		eligibility= request.POST['eligibility']
		prerequisite= request.POST['prerequisite']
		facility= request.POST['facilities']
		event_detail_docs=request.POST['event_detail_docs']
		if event=='':
			return render(request,'addrubrics.html', {'error':"Event is not selected"})	
		else:
			event = request.POST['event_name']
		if no_participant=='':
			return render(request,'addrubrics.html', {'error':"No Participant not filled!"})	
		else:
			no_participant= request.POST['no_participant']	
		if expected_participant=='':
			return render(request,'addrubrics.html', {'error':"No Participant not filled!"})	
		else:
			expected_participant =request.POST['expected_participant']						
		if event_level=='':
			return render(request,'addrubrics.html', {'error':"Event level field not selected"})	
		else:
			event_level= request.POST['event_level']			
		if eligibility=='':
			return render(request,'addrubrics.html', {'error':"Eligibility  field not selected"})	
		else:
			eligibility= request.POST['eligibility']			
		if prerequisite=='':
			return render(request,'addrubrics.html', {'error':"Prerequisite field not filled"})	
		else:
			prerequisite= request.POST['prerequisite']
			
		if facility=='':
			return render(request,'addrubrics.html', {'error':"Facility field not filled"})	

		else:
			facility= request.POST['facilities']

		if event_detail_docs=='':
			return render(request,'addrubrics.html', {'error':"File is not attached"})	

		else:
			event_detail_docs = request.POST['event_detail_docs']
			

		eventInstance = EventDetails(event=event,no_participant=no_participant,expected_participant=expected_participant,event_level=event_level,eligibility=eligibility,prerequisite=prerequisite,
			facility=facility,event_detail_docs=event_detail_docs)

		eventInstance.save()
		
		
		return render(request,'addrubrics.html',{'registered':'Event Successfully Registered!'})
def organiseEventFormData(request):
	if request.method=='POST':
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
			return render(request,'organise_event.html', {'error':"Event already Registered!"})	
		else:

			if event_title=='':
				return render(request,'organise_event.html', {'error':"Please Enter Event Title!"})	
			else :
				event_title = request.POST['event_title']

			if 	event_description =='':
				return render(request,'organise_event.html', {'error':"Please Enter Event Title!"})	
			else:
				event_description = request.POST['event_description']

			if event_category=='':	
				return render(request,'organise_event.html', {'error':"Please Select Event Category!"})		
			else: 
				event_category = request.POST['event_category']

			if org_name=='':
				return render(request,'organise_event.html', {'error':"Please Enter Org Name!"})				
			else:
				org_name = request.POST['org_by']
			if org_email=='':
				return render(request,'organise_event.html', {'error':"Please Enter Org Email!"})			
			else:
				org_email = request.POST['org_email']
			if org_mobile=='':
				return render(request,'organise_event.html', {'error':"Please Enter Org Mobile!"})	
			else :
				org_mobile = request.POST['mobile']
			if org_contact_person=='':
				return render(request,'organise_event.html', {'error':"Please Enter Contact Person Name!"})	
			else:
				org_contact_person = request.POST['person_name']
			if event_poster=='':
				return render(request,'organise_event.html', {'error':"Please Select Event Poster!"})
			else:
				event_poster = request.POST['event_poster']					
			if event_startdate=='':
				return render(request,'organise_event.html', {'error':"Please  Select Start Date!"})		
			else:
				event_startdate = request.POST['event_startdate']
			if event_enddate=='':
				return render(request,'organise_event.html', {'error':"Please Select End Date !"})				
			else:
				event_enddate = request.POST['event_enddate']
			event = OrganiseEvent(event_title = event_title,event_description=event_description,event_category=event_category,org_name=org_name,
									org_email=org_email,org_mobile=org_mobile,org_contact_person=org_contact_person,
									event_poster=event_poster,event_startdate=event_startdate,
									event_enddate = event_enddate) 	
			event.save()
			return render(request,'organise_event.html',{'event':'Event Successfully Registered!'})		
def addrubrics(request):
	eventDetails =  EventDetails.objects
	eventsOrganise = OrganiseEvent.objects
	context ={	'eventDetails':eventDetails,
				'eventsOrganise':eventsOrganise
			}
	return render(request,'addrubrics.html',context)
def organiseEvent(request):
	events = OrganiseEvent.objects
	return render(request,'organise_event.html',{'events':events})	
def eventEdit(request,id):
	event =get_object_or_404(OrganiseEvent,pk=id)
	#event =get_object_or_404(EventDetails,pk=id)
	return render(request,'sponsor_event.html',{'event':event})
def registeredEvent(request):
	events = OrganiseEvent.objects
	return render(request,'registered_event.html',{'events':events})
def indx(request):
	return  render(request,'organiser_index.html')
def form_name_view(request):
	form = forms.FormName()
	if request.method =='POST':
		form = forms.FormName(request.POST)
		form.save()
		if form.is_valid():
			print("Validation Success!!")
			print("name :" + form.cleaned_data['name'])
			print("Email: "+ form.cleaned_data['email'])
			print("Text:" + form.cleaned_data['text'])
	return render(request,'organiser.html',{ 'form':form})


def about(request):
	return  render(request,'pages/index.html')