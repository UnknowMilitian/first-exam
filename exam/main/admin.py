from django.contrib import admin
from .models import Product, ProductAccess


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    pass
