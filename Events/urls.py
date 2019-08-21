from django.urls import path

from Events import views 

urlpatterns = [
	path('',views.eventManager,name='Events'),
	path('eventDetails/<int:id>/',views.eventDetails,name='eventDetails')


]