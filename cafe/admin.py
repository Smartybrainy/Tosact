from django.contrib import admin
from .models import ContactEnquiries


@admin.register(ContactEnquiries)
class ContactEnquiriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name', 'email')
    list_filter = ['name', 'email']
    search_fields = ['name']
