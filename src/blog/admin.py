from django.contrib import admin
from .models import Gets


class GetsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'number',
        'email',
    ]
    list_display_links = [
        'name',
        'number',
        'email',
    ]
    search_fields = [
        'name',
        'number',
        'email',
    ]


# class ItemAdmin(ImportExportModelAdmin):
#    pass

admin.site.register(Gets, GetsAdmin)
