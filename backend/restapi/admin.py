from django.contrib import admin
from restapi.app.cards.models import Card
from restapi.app.cards.rules.models import CardRule

admin.site.register(Card)
admin.site.register(CardRule)