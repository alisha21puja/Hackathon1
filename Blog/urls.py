from django.urls import path



from Blog import views 

urlpatterns = [
	path('',views.addSlider,name='Blog'),




]