from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

# Create your views here.
class ListOrder(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer