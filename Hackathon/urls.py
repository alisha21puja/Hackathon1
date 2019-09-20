
from django.contrib import admin
from django.urls import path, include
from Blog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', include('home.urls'), name='home'),
    path('aboutus/', include('aboutus.urls'), name='aboutus'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls),

    path('Blog/', include('Blog.urls'), name='Blog'),
    path('Events/', include('Events.urls'), name='Events'),
    path('Organizer/', include('Organizer.urls'), name='Organizer'),
    path('Participant/', include('Participant.urls'), name='Participant'),
    path('Report/', include('Report.urls'), name='Report'),
    path('Sponsor/', include('Sponsor.urls'), name='Sponsor'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
