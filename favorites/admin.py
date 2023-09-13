from django.contrib import admin

from . import models


@admin.register(models.FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'product')
    list_display_links = ('pk', )
