from django.shortcuts import render
from rest_framework import viewsets
from .models import Collected
from .serializers import CollectedSerializer

# Create your views here.
class ListCollected(viewsets.ModelViewSet):
	queryset = Collected.objects.all()
	serializer_class = CollectedSerializer