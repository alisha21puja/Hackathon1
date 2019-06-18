from django.urls import path


from home import views 

urlpatterns = [
	path('',views.addSlider,name='home'),
	



]