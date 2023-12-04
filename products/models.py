from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.CASCADE)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    alt = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        unique=False,
        verbose_name='Alt text',
        help_text='format: required, max_length=300'
    )
    is_petfriendly = models.BooleanField()

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    special_notes = models.CharField(
     max_length=1000, null=True, blank=True)


class FavouritePlant(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    plant_name = models.CharField(
        max_length=100, null=True, blank=True)
    notes = models.CharField(max_length=1000, null=True, blank=True)
