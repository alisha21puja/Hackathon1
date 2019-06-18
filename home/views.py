from django.shortcuts import render


# Create your views here.



from .models import Slider


def addSlider(request):
	slide= Slider.objects
	return render(request,'index.html',{'slide':slide})
	


