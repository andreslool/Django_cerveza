from django.shortcuts import render
from rest_framework import viewsets
from .models import chela
from .serializers import chelaserializer

# Create your views here.

class chelaviewset(viewsets.ModelViewSet):
    serializer_class = chelaserializer
    queryset = chela.objects.all()

