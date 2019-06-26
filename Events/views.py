from django.shortcuts import render,get_object_or_404
from Organizer.models import OrganiseEvent

from django.utils import timezone
from django.utils.timezone import now
from django.db.models import Q
from datetime import date,timedelta

def eventManager(request):
	#events = OrganiseEvent.objects	

	starttime = timezone.now()
	today = date.today()+timedelta(days=1)
	#events = OrganiseEvent.objects.all()
	yesterday = today - timedelta(days=30)
	
	events = OrganiseEvent.objects.filter().order_by('event_enddate','event_startdate').reverse()

	eventcompleted = OrganiseEvent.objects.filter(event_enddate__month=yesterday.month).order_by('event_enddate').reverse()
	context = {
				'events':events,
				'today':today,
				'eventcompleted':eventcompleted

				#'eventdone':eventdone
	}

	return render(request,'events.html',context)


def eventDetails(request,id):

	today = date.today()
	events = OrganiseEvent.objects.filter(pk=id)
	
	return render(request,'eventDetails.html',{'events':events,'today':today})
