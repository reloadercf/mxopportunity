from django.shortcuts import render
from .models import Revista,Categorias
from articulos.serializers import CategoriaSerializer
from rest_framework import viewsets
# Create your views here.

class CategoriaRevistaViewSet(viewsets.ModelViewSet):
    queryset            =   Categorias.objects.all()
    serializer_class    =   CategoriaSerializer
    def get_queryset(self,*args,**kwargs):
        revista_origen  =       self.request.GET.get("r")
        queryset_list = super(CategoriaRevistaViewSet, self).get_queryset()
        if revista_origen:
            queryset_list = queryset_list.filter(revista_origen__nombre_revista=revista_origen) 
        return queryset_list