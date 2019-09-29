from django.urls import path

from django.conf import settings

from django.conf.urls.static import static
from Sponsor import views as views

urlpatterns = [
    path('', views.sponsor, name='sponsorIndex'),
    path('profile', views.profile, name='profile'),
    path('enquireInfoMail', views.enquireInfoMail, name='enquireInfoMail'),
    path('sponsor_event', views.sponsor_event, name='sponsor_event'),
    path('addsponsershipinfo', views.addsponsershipinfo, name='addsponsershipinfo'),
    path('addsponsership', views.addsponsership, name='addsponsership'),
    path('sponsored', views.sponsoredEvent, name='sponsoredEvent'),
    path('enquire', views.enquire, name='enquire'),
    path('enquire_event', views.enquire_event, name='enquire_event'),
    path('blogSponsor', views.blogSponsor, name='blog_sponsor'),
    path('blogSponsorWrite', views.writeBlogSponsor, name='blog_write_sponsor'),
    path('blogDetailsSpnsorship', views.blogDetailSponsor, name="blog_Sponsor"),
    path('upcoming/', views.events, name='upcoming'),
    path('event_details/<int:id>', views.event_details, name='event_details'),
    path('handlerequest/', views.handleRequest, name='handlerequest'),
    path('payAmount/', views.payAmount, name='payAmount'),
    path('amount/<int:id>', views.amount, name='amount'),
    path('transaction/<int:id>/', views.transaction, name='transaction'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
