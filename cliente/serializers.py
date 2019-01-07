from rest_framework import serializers
from .models import Planesvigentes,Cliente
from revista.models import Categorias,Revista
from articulos.serializers import SoloRevistaSerializer

class PlanSerializer(serializers.ModelSerializer):
    procedencia =   SoloRevistaSerializer(many=False,read_only=True)
    class Meta:
        model   =   Planesvigentes
        fields  =   '__all__'

class ClieteSerializer(serializers.ModelSerializer):
    revista_pertenencia =   SoloRevistaSerializer(many=False,read_only=True)
    class Meta:
        model   =   Cliente
        fields  =   '__all__'
