from django.db import models
from revista.models import Revista

# Create your models here.
#los choices
status_articulo_choice =(
    ("Publicado","Publicado"),
    ("No Publicado","No publicado")
)
video_choice=(
    ("youtube","youtube"),
    ("vimeo","vimeo"),
    ("sin video","sin video")
)
llamadas=(
    ("Contactar","Contactar"),
    ("Visitar","Visitar"),
    ("Compar","Comprar"),
    ("Llamar","Llamar")
)
#El modelo

class Articulo(models.Model):
    titulo                  =   models.CharField(max_length=50)
    en_portada              =   models.BooleanField(default=False)
    origen_revista          =   models.ForeignKey("revista.Revista", on_delete=models.CASCADE)
    categoria               =   models.CharField(max_length=100,blank=False,null=False)    
    imagen_destacada_uno    =   models.FileField(upload_to='articulos/uno/',blank=False)
    redactado_por           =   models.CharField(default="Equipo MX OPPORTUNITY",max_length=300,null=True,blank=True)
    status                  =   models.CharField(choices=status_articulo_choice,default="Publicado", max_length=50)
    cuerpo                  =   models.TextField(null=False,blank=False)
    imagen_destacada_dos    =   models.FileField(upload_to="articulos/dos/", max_length=100)
    video_tipo              =   models.CharField(choices=video_choice, default="sin video", max_length=50)
    urlvideo                =   models.URLField(blank=True,null=True)
    llamada_accion          =   models.CharField(choices=llamadas,max_length=50)
    imagen_llamada          =   models.FileField(upload_to="llamadas")
    url_llamada             =   models.URLField()
    cortesia_de             =   models.CharField(max_length=300,null=True,blank=True)
    fecha_mostrada          =   models.DateField(blank=False,null=False)
    fecha_publicacion       =   models.DateTimeField(blank=False,null=False)
    fecha_fin               =   models.DateTimeField(blank=False,null=False)
    fecha_creacion          =   models.DateTimeField(auto_now_add=True)
    fecha_modificacion      =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo