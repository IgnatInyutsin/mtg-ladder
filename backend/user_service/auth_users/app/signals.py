from django.dispatch import receiver
from djoser.signals import user_activated
from .models import Profile
from .models import PioneerProfile
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding:
        instance.is_active = False

@receiver(user_activated)
def activate_profile(user, request, **kwargs):
    Profile(user=user).save()
    PioneerProfile(user=user).save()