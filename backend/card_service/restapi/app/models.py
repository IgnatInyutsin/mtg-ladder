import uuid
from django.db import models
from multiselectfield import MultiSelectField

COLORS = (("B", "Black"),
          ("G", "Green"),
          ("R", "Red"),
          ("U", "Blue"),
          ("W", "White"))
TYPES = (("Artifact", "Artifact"),
          ("Card", "Card"),
           ("Conspiracy", "Conspiracy"),
            ("Creature", "Creature"),
             ("Dragon", "Dragon"),
              ("Dungeon", "Dungeon"),
               ("Eaturecray", "Eaturecray"),
                ("Elemental", "Elemental"),
                 ("Elite", "Elite"),
                  ("Emblem", "Emblem"),
                   ("Enchantment", "Enchantment"),
                    ("Ever", "Ever"),
                     ("Goblin", "Goblin"),
                      ("Hero", "Hero"),
                       ("Instant", "Instant"),
                        ("Jaguar", "Jaguar"),
                         ("Knights", "Knights"),
                          ("Land", "Land"),
                           ("Phenomenon", "Phenomenon"),
                            ("Plane", "Plane"),
                             ("Planeswalker", "Planeswalker"),
                              ("Scariest", "Scariest"),
                               ("Scheme", "Scheme"),
                                ("See", "See"),
                                 ("Sorcery", "Sorcery"),
                                  ("Specter", "Specter"),
                                   ("Summon", "Summon"),
                                    ("Token", "Token"),
                                     ("Tribal", "Tribal"),
                                      ("Vanguard", "Vanguard"),
                                       ("Wolf", "Wolf"),
                                        ("You’ll", "You’ll"),
                                         ("instant", "instant"))

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    mana_value = models.IntegerField(blank=True, null=True)
    mana_cost = models.CharField(max_length=256, blank=True, null=True)
    colors = MultiSelectField(choices=COLORS, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    types = MultiSelectField(choices=TYPES, blank=True, null=True)
    power = models.CharField(max_length=256, blank=True, null=True)
    toughness = models.CharField(max_length=256, blank=True, null=True)
    loyalty = models.CharField(max_length=256, blank=True, null=True)
    scryfall_id = models.CharField(max_length=256)
    english_text = models.TextField(blank=True, null=True)
    english_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return  self.name