from django.shortcuts import render
from rest_framework import generics, viewsets, status
from .models import Person
from .serializers import UserSerializer

# Create your views here.

class ListUser(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = UserSerializer