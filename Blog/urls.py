from django.urls import path


from Blog import views

urlpatterns = [
    path('', views.blogs, name='Blog'),
<<<<<<< HEAD
    path('/<int:id>', views.blogDetail, name='blogdetails')



=======
    path('<int:id>', views.blogDetail, name='blogdetails')
>>>>>>> 00486efd62bd717f2eaff3e6c9f80a737c54bef9
]
