from django.contrib import admin
from .models import Menu, Product


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Menu, MenuAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'descreption', 'price', 'weight')


admin.site.register(Product, ProductAdmin)