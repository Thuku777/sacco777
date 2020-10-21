from django.contrib import admin

from .models import *

admin.site.register(Address)
admin.site.register(Contact_heading)

class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'phone', 'subject', 'contact_date',)
  list_display_links = ('name',)
  search_fields = ('name', 'email',)
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
