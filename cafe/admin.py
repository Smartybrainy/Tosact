from django.contrib import admin
from .models import ContactEnquiries, Blog, Like


@admin.register(ContactEnquiries)
class ContactEnquiriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name', 'email')
    list_filter = ['name', 'email']
    search_fields = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "slug")
    list_display_links = ("user", "title", "slug")
    list_per_page = 50
    prepopulated_fields = {'slug': ("title", )}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Like)