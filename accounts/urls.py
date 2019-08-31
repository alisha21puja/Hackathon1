from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', views.indx, name='accounts'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('login', views.loginn, name='login'),
    path('organiser', include('Organizer.urls'), name='organiserIndex'),
    path('sponsor', include('Sponsor.urls'), name='sponsorIndex'),
    path('participant/', include('Participant.urls'), name='participantIndex'),
]
