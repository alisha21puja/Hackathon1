from django.urls import path

from Report import views as ve

urlpatterns = [
	path('',ve.about,name='about'),



]