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


# Register the configured admin classes for each model
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Stock)
admin.site.register(FavouritePlant)


