from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Person

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = (
			'username', 
			'no_hp', 
			'password', 
			'date_joined', 
			'last_login', 
			'first_name',
			'alamat',
			)

	def create(self, validated_data):
		user = Person.objects.create_user(**validated_data)
		Token.objects.create(user=user)
		return user

	