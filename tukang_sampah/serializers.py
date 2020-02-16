from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = (
			'collected_trash_paper', 
			'collected_trash_food', 
			'collected_trash_plastic', 
			'user'
			)