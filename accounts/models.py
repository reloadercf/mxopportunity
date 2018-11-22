from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from  .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from revista.models import Revista


class Perfil(models.Model):
    user        = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)    
    revista     = models.ForeignKey(Revista,related_name='revista_perfil',blank=True,null=True, on_delete=models.CASCADE)
    slug        = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def username(self):
        return self.user.username


# @property
    def nombre_completo(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Perfil)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Perfil.objects.get_or_create(user=kwargs.get('instance'))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
