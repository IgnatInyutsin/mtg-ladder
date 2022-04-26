from django.dispatch import receiver
from django.db.models.signals import pre_save
from restapi.app.models import Card
from restapi.app.rules.models import CardRule
import uuid

# генерируем uuid для Card
@receiver(pre_save, sender=Card)
def generate_uuid_by_name(sender, instance, **kwargs):
    if instance._state.adding:
        instance.id = uuid.uuid5(uuid.NAMESPACE_DNS, instance.name)

# генерируем uuid для CardRule
@receiver(pre_save, sender=CardRule)
def generate_uuid_by_name(sender, instance, **kwargs):
    if instance._state.adding:
        instance.id = uuid.uuid5(uuid.NAMESPACE_DNS, instance.card.name + " " + instance.date.isoformat())