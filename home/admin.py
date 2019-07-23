from django.contrib import admin

# Register your models here.




from .models import  Slider,OurPartner


class SliderAdmin(admin.ModelAdmin):
	list_display = ('id','slide1','slide2','slide3')
	list_display_links = ('id','slide1')
	list_filter =('slide1',)
	list_editable=('slide2',)
	search_fields=('slide1','slide2')
	list_per_page=2





class OurPartnerAdmin(admin.ModelAdmin):
	list_display = ('id','organisationName','country','orgLogo','maplocation')
	# list_display_links = ('id','organisationName')
	# list_filter =('organisationName',)
	# list_editable=('organisationName',)
	# # search_fields=('slide1','slide2')
	list_per_page=2


admin.site.register(Slider,SliderAdmin)


admin.site.register(OurPartner,OurPartnerAdmin)

