from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(default="")

    def __str__(self):
        return "Profile of " + self.user.username

class PioneerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pioneer")
    elo = models.IntegerField(default=1500)
    max_elo = models.IntegerField(default=1500)
    min_elo = models.IntegerField(default=1500)

    def __str__(self):
        return "Pioneer Profile of " + self.user.username