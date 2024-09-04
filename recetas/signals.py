from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Receta

@receiver(post_save, sender=Receta)
def set_codigo_de_receta(sender, instance, created, **kwargs):
    if created:
        instance.codigo_de_receta = f"{instance.user.id}-{instance.id}"
        instance.save()