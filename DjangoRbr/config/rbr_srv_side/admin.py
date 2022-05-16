from django.contrib import admin
from .models import Server
# Register your models here.


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_fields = ['ip_address', 'description', 'name', 'server_is_active']
