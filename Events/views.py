from django.shortcuts import render

# Create your views here.


def eventManager(request):
	return render(request,'events.html')

