from .models import Perfil
from django.contrib.auth.models import User
from rest_framework import serializers
from articulos.serializers import RevistaSerializer

class PerfilSerializer(serializers.ModelSerializer):
    revista=RevistaSerializer(many=False,read_only=True)
    class Meta:
        model = Perfil
        fields = ['revista']

class UserSerializer(serializers.ModelSerializer):
	profile = PerfilSerializer(many=False, read_only=True)
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'email', 'id', 'password', 'profile']
	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User.objects.create(**validated_data)
		user.set_password(password)
		user.save()
		return user