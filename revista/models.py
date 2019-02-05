from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre_categoria        =   models.CharField(max_length=80)
    revista_origen          =   models.ForeignKey("revista.Revista", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_categoria 
    

class Revista(models.Model):
    nombre_revista          =   models.CharField(max_length=80, blank=False, null=False)
    logo                    =   models.TextField()
    descripcion             =   models.TextField()
    def __str__(self):
        return self.nombre_revista
