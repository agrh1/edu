from django.shortcuts import render
from rest_framework import generics
from .serializator import ServerSerializer, ServerShortSerializer
from .models import Server
# Create your views here.


class ServerViewSet(generics.ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerAddView(generics.CreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerShortViewSet(generics.ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerShortSerializer


