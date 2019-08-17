from django.shortcuts import render

from Blog.models import BlogsInfo

# Create your views here
from Organizer.models import OrganiseEvent,EventDetails
from Participant.models import ParticipateEvent
from accounts.models import  UserProfile
from django.contrib.auth.models import User
from django.utils import timezone
from Blog.models import BlogsInfo


def about(request):
	return  render(request,'participant_index.html')


def participate(request):
	even = EventDetails.objects
	return render(request,'participant_index.html',{'even':even})


def part_profile(request):
	return render(request,'part_profile.html',{})

def part_editProfile(request):
	part_profiles=UserProfile.objects	
	return render(request,'part_editProfile.html',{'part_profiles':part_profiles})

def part_updateProfile(request):
	if request.method=='POST':	
		submitbutton = request.POST.get('Submit')
		if submitbutton :
			user = request.POST['user']	
			fname =  request.POST['fname']
			lname =  request.POST['lname']
			email =  request.POST['email']
			
			profiles=User(id=request.user.id,username=user,first_name= fname,last_name=lname,email=email)
			profiles.save()
			profiles.refresh_from_db()		
			edit_profile=UserProfile.objects
			return render(request,'part_profile.html',{'part_profile':edit_profile})


def deleteparticipant(request):
	User.objects.filter(username=request.user.username).delete()
	#messages.success(request,'Profile have been Successfully deleted')
	return render(request, 'login.html' ,{'error':'Profile have been Successfully deleted'})

def event_details(request):
	events = OrganiseEvent.objects
	return render(request,'event_details.html',{'events':events})

def participated_event(request):
	part_event = ParticipateEvent.objects.filter(us= request.user.id)
	events = OrganiseEvent.objects.filter(us= request.user.id)
	return render(request,'participated_event.html',{'part_event':part_event})
