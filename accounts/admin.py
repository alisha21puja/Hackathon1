from django.contrib import admin
from django.contrib.admin.models import LogEntry
admin.site.register(LogEntry)


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_type', 'action_flag')
    list_display_links = ('user', 'action_type')
    search_fields = ('action_type',)
    readonly_fields = ('content_type',
                       'user',
                       'action_time',
                       'object_id',
                       'object_repr',
                       'action_flag',
                       'change_message'
                       )

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(LogEntryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
