from django.contrib import admin

from products.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', ('price', 'quantity'), 'description', 'category', 'image')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)
