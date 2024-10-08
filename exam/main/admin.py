from django.contrib import admin
from .models import Product, ProductAccess, Lesson, LessonProgress


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    pass
