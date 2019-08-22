from django.shortcuts import render


# Create your views here.

from Organizer.models import OrganiseEvent

from django.utils import timezone
from django.utils.timezone import now
from django.db.models import Q
from datetime import date,timedelta

from .models import Slider,OurPartner


def addSlider(request):
	slide= Slider.objects
	ourPartner = OurPartner.objects


	starttime = timezone.now()
	slide= Slider.objects
	today = date.today()+timedelta(days=1)
	
	yesterday = today - timedelta(days=30)
	
	events = OrganiseEvent.objects.filter().order_by('event_enddate','event_startdate').reverse()

	eventcompleted = OrganiseEvent.objects.filter(event_enddate__month=yesterday.month).order_by('event_enddate').reverse()
	context = {
				'events':events,
				'today':today,
				'eventcompleted':eventcompleted,
				
				'slide':slide,
				'ourPartner':ourPartner

				#'eventdone':eventdone
	}



	return render(request,'index.html',context)



	

def eventManager(request):
	

	

	return render(request,'index.html')

