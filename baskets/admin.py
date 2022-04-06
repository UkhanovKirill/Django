from django.contrib import admin
from baskets.models import Basket


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'create_timestamp')
    readonly_fields = ('create_timestamp',)
    extra = 0
