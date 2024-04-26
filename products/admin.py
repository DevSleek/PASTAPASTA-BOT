from django.contrib import admin
from .models import Category, Product, Card


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'photo', 'descreption', 'price', 'weight')


admin.site.register(Product, ProductAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')


admin.site.register(Card, CardAdmin)