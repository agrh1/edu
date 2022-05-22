from django.contrib import admin
from .models import Server, ServerData
# Register your models here.


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'description', 'name', 'server_is_active']


@admin.register(ServerData)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'data']