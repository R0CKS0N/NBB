from django.contrib import admin
from .models import Gets


class GetsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'number',
        'Email',
        'label',
    ]
    list_display_links = [
        'name',
        'number',
        'Email',
        'label',
    ]
    list_filter = [
        'label',
    ]
    search_fields = [
        'name',
        'number',
        'Email',
        'label',
    ]


# class ItemAdmin(ImportExportModelAdmin):
#    pass

admin.site.register(Gets, GetsAdmin)
