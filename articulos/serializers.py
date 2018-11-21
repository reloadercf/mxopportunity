from rest_framework import serializers
from .models import Articulo
from revista.models import Categorias,Revista

class RevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Revista
        fields  =   '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   RevistaSerializer(many=False,read_only=True)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   RevistaSerializer(many=False,read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   '__all__'