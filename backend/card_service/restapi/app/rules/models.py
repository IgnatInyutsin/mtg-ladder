from django.db import models
import uuid

class CardRule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    text = models.TextField()
    card = models.ForeignKey('Card',  on_delete=models.CASCADE, related_name="rules")

    def __str__(self):
        return self.card.name + " " + self.date.isoformat()