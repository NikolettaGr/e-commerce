from django.db import models
from products.models import Product
from profiles.models import User


class Wishlist(models.Model):
    """Model for a wishlist."""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='wishlist'
    )
    products = models.ManyToManyField(
        Product,
        blank=True,
        related_name='wishlist'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
