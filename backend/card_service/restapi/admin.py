from django.contrib import admin
from restapi.app.models import Card
from restapi.app.rules.models import CardRule

admin.site.register(Card)
admin.site.register(CardRule)