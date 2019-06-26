from django.urls import path
from Sponsor import views as views

urlpatterns = [
	path('',views.sponsor,name='sponsorIndex'),
	path('/sponsored/',views.sponsoredEvent,name='sponsoredEvent'),
	path('/upcoming',views.sponsorUpComing,name='sponsorUpComing'),
	path('/enquire',views.enquire,name='enquire'),
	path('/blogSponsor',views.blogSponsor,name='blog_sponsor'),
	path('/blogSponsorWrite',views.writeBlogSponsor,name='blog_write_sponsor'),
	path('/sponsored/<int:id>',views.sponsorEventUpdate,name='sponsorEdit'),
	path('/event/<int:id>',views.sponsorEventDetails,name='sponsorEventDetails'),



	



]