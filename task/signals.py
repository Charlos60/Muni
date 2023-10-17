from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Multas

#JOB sumar saldo
@receiver(post_save, sender=Multas)
def actualizar_saldo_usuario(sender, instance, created, **kwargs):
    if created:  # Solo realiza esta acción si se crea una nueva multa
        usuario = instance.usuario
        usuario.saldo += instance.saldo
        usuario.save()

#Job resatar saldo
@receiver(post_delete, sender=Multas)
def restar_saldo_usuario(sender, instance, **kwargs):
    usuario = instance.usuario
    usuario.saldo -= instance.saldo
    usuario.save() 