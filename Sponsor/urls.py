from django.urls import path

from django.conf import settings

from django.conf.urls.static import static
from Sponsor import views as views

urlpatterns = [
	path('',views.sponsor,name='sponsorIndex'),
	path('/sponsored/',views.sponsoredEvent,name='sponsoredEvent'),
	path('/upcoming/',views.sponsorUpComing,name='sponsorUpComing'),
	path('/enquiree/<int:id>/',views.enquireInfo,name='enquiree'),
	path('/enquire',views.enquire,name='enquire'),
	path('/blogSponsor',views.blogSponsor,name='blog_sponsor'),
	path('/blogSponsorWrite',views.writeBlogSponsor,name='blog_write_sponsor'),
	path('/sponsored/<int:id>',views.sponsorEventUpdate,name='sponsorEdit'),
	path('/event/<int:id>',views.sponsorEventDetails,name='sponsorEventDetails'),
	path('/sponsorDetails/<int:id>',views.sponsorEventDet,name='sponsorDetails'),
	path('/eventParticipate/<int:id>/',views.eventInfo,name='eventParticipate'),
	path('/enquireInfoMail',views.enquireInfoMail,name='enquireInfoMail'),



	



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)