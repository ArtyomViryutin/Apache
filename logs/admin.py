from django.contrib import admin
from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'ip', 'date')
    search_fields = ('uri',)
    list_filter = ('date',)


admin.site.site_title = 'Apache logs'
admin.site.site_header = 'Apache logs'

