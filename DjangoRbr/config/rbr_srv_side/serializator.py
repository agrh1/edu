from rest_framework import serializers
from .models import Server, ServerData


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ['ip_address', 'description', 'name', 'server_is_active']


class ServerShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ['ip_address', 'server_is_active']


class ServerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerData
        fields = ['ip_address', 'data']