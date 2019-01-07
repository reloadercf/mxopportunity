from django.shortcuts import render
from .models import Articulo
from revista.models import Revista
from .serializers import ArticuloSerializer,EspecialArticulo
from rest_framework import viewsets
from django.db.models import Q
from datetime import *
# Create your views here.

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

    def get_queryset(self,*args,**kwargs):
        categoria       =       self.request.GET.get("q")
        origen_revista  =       self.request.GET.get("r")
        titulo          =       self.request.GET.get("slug")
        queryset_list = super(ArticuloViewSet, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(categoria=categoria)
        if origen_revista:
            queryset_list = queryset_list.filter(origen_revista__nombre_revista=origen_revista)
        if titulo:
            queryset_list = queryset_list.filter(slug=titulo)
        return queryset_list

class EspecialArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = EspecialArticulo

    def get_queryset(self,*args,**kwargs):
        categoria       =       self.request.GET.get("q")
        origen_revista  =       self.request.GET.get("r")
        titulo          =       self.request.GET.get("slug")
        portada         =       self.request.GET.get("portada")
        status          =       self.request.GET.get("status")

        queryset_list = super(EspecialArticuloViewSet, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(categoria=categoria)
        if origen_revista:
            queryset_list = queryset_list.filter(origen_revista__nombre_revista=origen_revista)
        if titulo:
            queryset_list = queryset_list.filter(slug=titulo)
        if portada:
            queryset_list = queryset_list.filter(en_portada=portada)
        if status:
            queryset_list = queryset_list.filter(status=status)
        return queryset_list
