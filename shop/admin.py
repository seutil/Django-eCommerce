from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


admin.site.site_title = 'eCommerce'
admin.site.site_header = 'Административная панель'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', )


class ManufactureProductsInline(admin.TabularInline):
    model = models.Product


@admin.register(models.Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', )
    inlines = [ManufactureProductsInline]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'manufacture')
    list_display_links = ('name',)
    list_filter = ('category', 'manufacture')
    search_fields = ('name', )
    save_on_top = True


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')
    list_display_links = ('title', )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" alt="{obj.title}" height="150">')

    get_image.short_description = 'Изображение'
