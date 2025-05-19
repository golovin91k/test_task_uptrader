from django.contrib import admin
from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'menu', 'parent')
