from django.shortcuts import render,get_object_or_404

from Blog.models import BlogsInfo

from Organizer.models import 	EventDetails,SponsorShip,EventDetails
from django.utils import timezone

def sponsor(request):
	return  render(request,'sponsor_index.html')

def sponsoredEvent(request):
	sponsors =SponsorShip.objects
	event=EventDetails.objects
	return render(request,'sponsor_event.html',{'sponsors':sponsors,'event':event})

def sponsorUpComing(request):
	return render(request,'sponsor_up_coming.html')



def sponsorEventUpdate(request,id):
	sponsors =get_object_or_404(SponsorShip,pk=id)
	return render(request,'sponsor_event.html',{'sponsor':sponsor})



def sponsorEventDetails(request,id):
	event = get_object_or_404(EventDetails, pk=id)


	return render(request,'sponsor_event.html')


def enquire(request):
	return render(request,'sponsor_enquire.html')



def blogSponsor(request):
	 return render(request,'blog_write_sponsor.html')





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

