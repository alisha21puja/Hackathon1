from django.shortcuts import render, get_object_or_404

# Create your views here.


from .models import BlogsInfo


def blogs(request):
    blog = BlogsInfo.objects
    return render(request, 'blog.html', {'blog': blog})


def blogDetail(request, id):

    detailblog = get_object_or_404(BlogsInfo, pk=id)
    return render(request, 'blogdetails.html', {'blog': detailblog})
