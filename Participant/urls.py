from django.urls import path




from Participant import views as ve

urlpatterns = [
	path('',ve.about,name='about'),
	



]