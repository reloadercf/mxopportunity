from django.shortcuts import render
from .models import Articulo
from revista.models import Revista
from .serializers import ArticuloSerializer
from rest_framework import viewsets
from .pagination import ArticlePagination
# Create your views here.

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    pagination_class = ArticlePagination

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