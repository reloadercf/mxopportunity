from rest_framework import serializers
from .models import Articulo
from revista.models import Categorias,Revista

class SoloRevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista']

class RevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Revista
        fields  =   '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   SoloRevistaSerializer(many=False,read_only=True)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   SoloRevistaSerializer(many=False,read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   '__all__'

class EspecialArticulo(serializers.ModelSerializer):
    origen_revista  =   SoloRevistaSerializer(many=False,read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['slug','en_portada','origen_revista','titulo','categoria','imagen_destacada_uno','status','fecha_fin']