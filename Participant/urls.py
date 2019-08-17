from django.urls import path

from django.conf import settings


from Participant import views as ve

urlpatterns = [
	path('',ve.about,name='participantIndex'),
	path('',ve.participate,name='participate'),
	path('/part_profile',ve.part_profile,name='part_profile'),
	path('/part_editProfile',ve.part_editProfile,name='part_editProfile'),
	path('/part_updateProfile',ve.part_updateProfile,name='part_updateProfile'),
	path('/deleteparticipant',ve.deleteparticipant,name='deleteparticipant'),
	path('/event_details',ve.event_details,name='event_details'),
	path('/participated_event',ve.participated_event,name='participated_event'),


	



]
