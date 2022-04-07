from django.contrib import admin
from restapi.app.cards.models import *

admin.site.register(Card)
admin.site.register(CardRule)