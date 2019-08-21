from django.urls import path

from aboutus import views

urlpatterns = [
    path('', views.addAboutSection, name='aboutus'),
    path('contact', views.contacts, name='contact'),
]
