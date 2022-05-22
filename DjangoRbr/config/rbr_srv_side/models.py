from django.db import models

# Create your models here.


class Server(models.Model):
    name = models.CharField('name', max_length=255)
    ip_address = models.GenericIPAddressField('íp_address', max_length=16, default='0.0.0.0', unique=True)
    description = models.TextField('description', max_length=255, default='no_description')
    server_is_active = models.BooleanField('server_is_active', default=False)

    class Meta:
        managed = True
        verbose_name = 'Server'


class ServerData(models.Model):
    ip_address = models.ForeignKey("Server", on_delete=models.CASCADE, to_field="ip_address")
    data = models.TextField()

    class Meta:
        managed = True
        verbose_name = 'ServerData'
