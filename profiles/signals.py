"""Signals for the profiles app."""
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import UserProfile
from django.contrib.auth.models import User
from wishlist.models import Wishlist


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        Wishlist.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    instance.wishlist.save()
