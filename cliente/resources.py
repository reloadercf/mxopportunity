from import_export import  resources
from import_export.fields import Field
from .models import Planesvigentes,Cliente

class ClienteResource(resources.ModelResource):
    class Meta:
        model=Cliente

class PlanesResource(resources.ModelResource):
    class Meta:
        model=Planesvigentes
