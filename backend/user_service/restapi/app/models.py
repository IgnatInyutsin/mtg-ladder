from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

class PioneerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    elo = models.IntegerField(default=1500)
    max_elo = models.IntegerField(default=1500)
    min_elo = models.IntegerField(default=1500)