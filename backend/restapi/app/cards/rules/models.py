from django.db import models

class CardRule(models.Model):
    date = models.DateField()
    text = models.TextField()
    card = models.ForeignKey('Card',  on_delete=models.CASCADE, related_name="rules")

    def __str__(self):
        return self.card.name + " " + self.date.isoformat()