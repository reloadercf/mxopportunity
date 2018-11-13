from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from  .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver



class Perfil(models.Model):
    correo      = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto        = models.ImageField(upload_to='images', blank=True, null=True)
    biografia   =models.TextField(blank=True, null=True)
    telefono    =models.CharField(blank=True,null=True, max_length=20)
    nombre      =models.CharField(blank=True,null=True,max_length=100)
    facebook    =models.URLField(blank=True,null=True)
    instagram   =models.URLField(blank=True,null=True)
    twitter     =models.URLField(blank=True,null=True)
    intereses   =models.TextField()
    slug        = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.correo.username

    @property
    def username(self):
        return self.correo.username


# @property
    def nombre_completo(self):
        return '%s %s' % (self.correo.first_name, self.correo.last_name)


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Perfil)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Perfil.objects.get_or_create(correo=kwargs.get('instance'))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
