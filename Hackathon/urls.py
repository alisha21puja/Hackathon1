
from django.contrib import admin
from django.urls import path, include
from Blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	path('',include('Organizer.urls')),
	path('Blog',views.addSlider,name='Blog'),
    path('admin/', admin.site.urls),
    path('Blog',include('Blog.urls')),
    path('Participant',include('Participant.urls')),
    path('Report',include('Report.urls'),),
    path('Sponsor',include('Sponsor.urls')),
    


   ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)