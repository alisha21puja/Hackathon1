from django.contrib import admin

# Register your models here.


from .models import AboutDescription, TeamInfo, OurServices, Contact


admin.site.register(AboutDescription)

admin.site.register(TeamInfo)

admin.site.register(OurServices)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
