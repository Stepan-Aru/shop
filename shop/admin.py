from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'on_stock', 'get_html_photo', 'is_sale')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('is_sale',)
    list_filter = ('is_sale',)
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'description', 'photo', 'price', 'on_stock', 'is_sale', 'cat')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')

    get_html_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
