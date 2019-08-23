from django.urls import path

from django.conf import settings

from django.conf.urls.static import static
from Sponsor import views as views

urlpatterns = [
	path('',views.sponsor,name='sponsorIndex'),
	path('profile',views.profile,name='profile'),
	path('enquireInfoMail',views.enquireInfoMail,name='enquireInfoMail'),
	path('sponsor',views.sponsor_event,name='sponsor'),
	path('sponsored',views.sponsoredEvent,name='sponsoredEvent'),
	path('enquire',views.enquire,name='enquire'),
	path('enquire_event',views.enquire_event,name='enquire_event'),
	path('blogSponsor',views.blogSponsor,name='blog_sponsor'),
	path('blogSponsorWrite',views.writeBlogSponsor,name='blog_write_sponsor'),
	path('upcoming/',views.events,name='upcoming'),
	path('event_details/<int:id>',views.event_details,name='event_details'),
	

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)