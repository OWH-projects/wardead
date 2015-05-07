from django.contrib import admin
from wardead.models import *

class WarDeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'homecity', 'homecounty', 'date', 'homestate', 'unit',)
    search_fields = ('name', 'homecounty', )
    list_filter = ('war', 'homestate', 'homecounty', )
    date_hierarchy = 'date'

admin.site.register(WarDead, WarDeadAdmin)
