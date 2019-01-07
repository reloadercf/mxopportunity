from django.shortcuts import render
from .models import Cliente,Planesvigentes
from .serializers import ClieteSerializer,PlanSerializer
from rest_framework import viewsets
from .pagination import ClientePagination
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset            =   Cliente.objects.all()
    serializer_class    =   ClieteSerializer
    pagination_class    =   ClientePagination
    def get_queryset(self,*args,**kwargs):
        origen_revista  =   self.request.GET.get("r")
        nombre_cliente  =   self.request.GET.get("cliente")
        queryset_list   =   super(ClienteViewSet, self).get_queryset()
        if origen_revista:
            queryset_list   =queryset_list.filter(revista_pertenencia__nombre_revista=origen_revista)
        if nombre_cliente:
            queryset_list   =queryset_list.filter(nombre_patrocinador=nombre_cliente)    
        return queryset_list
    
class PlanesViewSet(viewsets.ModelViewSet):
    queryset            =   Planesvigentes.objects.all()
    serializer_class    =   PlanSerializer
    pagination_class    =   ClientePagination
    def get_queryset(self,*args,**kwargs):
        origen_revista  =   self.request.GET.get("r")
        nombre_plan  =   self.request.GET.get("plan")
        queryset_list   =   super(PlanesViewSet, self).get_queryset()
        if origen_revista:
            queryset_list   =queryset_list.filter(procedencia__nombre_revista=origen_revista)
        if nombre_plan:
            queryset_list   =queryset_list.filter(plan=nombre_plan)    
        return queryset_list
