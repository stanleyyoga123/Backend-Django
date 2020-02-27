from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = (
			'order_trash_paper',
			'order_trash_plastic',
			'order_trash_food',
			'user',
			)