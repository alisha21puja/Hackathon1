from django.shortcuts import render

# Create your views here
from Organizer.models import OrganiseEvent,EventDetails
def about(request):
	return  render(request,'participant_index.html')


def participate(request):
	even = EventDetails.objects
	return render(request,'participant_index.html',{'even':even})
