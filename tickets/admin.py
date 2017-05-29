from django.contrib import admin
from . models import Ticket

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['pub_date']

admin.site.register(Ticket, TicketAdmin)