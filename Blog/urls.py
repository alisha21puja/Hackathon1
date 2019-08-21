from django.urls import path


from Blog import views

urlpatterns = [
    path('', views.blogs, name='Blog'),
    path('<int:id>', views.blogDetail, name='blogdetails')
]
