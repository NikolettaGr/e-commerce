from django.contrib import admin
from .models import *


# Configure the admin interface for the Painting model
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'sku',
        'rating',
        'image',
    )

    ordering = ('sku',)


# Configure the admin interface for the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
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


# Register the configured admin classes for each model
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(FavouritePlant, FavouritePlantAdmin)



