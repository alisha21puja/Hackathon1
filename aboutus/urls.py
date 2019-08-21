from django.urls import path

from aboutus import views

urlpatterns = [
    path('', views.addAboutSection, name='aboutus'),
<<<<<<< HEAD
    path('/contact', views.contacts, name='contact'),
=======
    path('contact', views.contacts, name='contact'),
>>>>>>> 00486efd62bd717f2eaff3e6c9f80a737c54bef9
]
