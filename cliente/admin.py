from django.contrib import admin
from .models import Cliente,Planesvigentes
from import_export.admin import ImportExportModelAdmin
from .resources import ClienteResource,PlanesResource


@admin.register(Cliente)
class AdminCliente(ImportExportModelAdmin):
    resource_class = ClienteResource
    list_display=('nombre_patrocinador','activo','revista_pertenencia','razonsocial','terminocontrato','plan_contratado','fecha_modificacion','telefono','correo')

@admin.register(Planesvigentes)
class AdminPlanes(ImportExportModelAdmin):
    resource_class = PlanesResource
    list_display=('plan','procedencia','caracteristicas',)
