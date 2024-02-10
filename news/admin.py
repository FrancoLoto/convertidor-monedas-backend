from django.contrib import admin

from .models import New


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_read', 'created_at')
    list_display_links = ('title',)
    search_fields = ('title', 'content', 'slug')
    list_per_page = 25


admin.site.register(New, NewAdmin)
