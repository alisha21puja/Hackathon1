from django.urls import path
from django.conf import settings

from django.conf.urls.static import static
from Organizer import views

urlpatterns = [
	path('',views.indx,name='organiserIndex'),
	path('/organiseEvent',views.organiseEvent,name='organiseEvent'),
	path('/formpage/',views.form_name_view,name='form_name'),
	path('/organiseEventFormData',views.organiseEventFormData,name="organiseEventFormData"),
	path('/registeredEvent',views.registeredEvent,name='registeredevent'),
	path('/eventRegistered/<int:id>',views.eventEdit,name='eventEdit'),
	path('/eventUpdate/<int:id>',views.eventUpdate,name='eventupdate'),
	path('/addEventDetails',views.addrubrics,name='addEventDetails'),
	path('/editRubrics/<int:id',views.returnEditRubrics,name='editRubrics'),
	
	path('/evenDetailsUpdate/<int:id>',views.evenDetailsUpdate,name='evenDetailsUpdate'),
	path('/addEvent',views.eventDetails,name='eventdetails'),
	path('/shareResourcese',views.shareResource,name='shareResource'),
	path('/Resource',views.resource,name='Resource'),
	path('/blog',views.blog,name='blog'),
	path('/WriteBlog',views.writeBlogs,name='WriteBlog'),
	path('/sponsorShip',views.sponsorShip,name='sponsorShip'),
	path('/sponsorShipDetails',views.sponsorShipDetails,name='sponsorShipDetails'),
	

			




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)