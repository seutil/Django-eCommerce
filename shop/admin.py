from django.contrib import admin

from . import models


admin.site.site_title = 'eCommerce'
admin.site.site_header = 'Административная панель'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', )


class ManufactureProductsInline(admin.TabularInline):
    model = models.Product
    extra = 1


@admin.register(models.Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', )
    inlines = [ManufactureProductsInline]


class ProductImagesInline(admin.TabularInline):
    model = models.ProductImage
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'manufacture')
    list_display_links = ('name',)
    list_filter = ('category', 'manufacture')
    search_fields = ('name', )
    inlines = [ProductImagesInline]
    save_on_top = True


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'get_image', 'product')
    list_display_links = ('get_title', 'get_image')
    list_filter = ('product', )
