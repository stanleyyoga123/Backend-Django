from rest_framework import serializers
from .models import Collected

class CollectedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Collected
		fields = (
			'collected_trash_paper', 
			'collected_trash_food', 
			'collected_trash_plastic', 
			'user'
			)