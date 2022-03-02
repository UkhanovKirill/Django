from django.contrib import admin
from baskets.models import Basket


class BasketAdminInline(admin.TabularInline):
    model = Basket
    readonly_fields = ('create_timestamp',)
    extra = 0
