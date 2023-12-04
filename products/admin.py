from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin for the Category model."""
    list_display = ('name', 'friendly_name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin for the Category model."""
    list_display = (
        'name',
        'category',
        'price',
        'sku',
        'rating',
        'image',
    )


# Configure the admin interface for the Stock model
class StockAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity',
        'special_notes',
    )


# Configure the admin interface for the FavouritePlant model
class FavouritePlantAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'plant_name',
        'notes',
    )


admin.site.register(Stock, StockAdmin)
admin.site.register(FavouritePlant, FavouritePlantAdmin)
