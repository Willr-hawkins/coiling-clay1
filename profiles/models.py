from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

from products.models import Product

class UserProfile(models.Model):
    """
    A user profile model for mantaining defualt
    delivery information and order history.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

class Wishlist(models.Model):
    """ 
    Model to represents a user's wishlist.
    Each user can have multiple wishlist's,
    with unique names. 
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='wishlists')
    wishlist_name = models.CharField(max_length=80)
    # Users can add a decriptive note to their wishlist
    wishlist_note = models.TextField(max_length=150, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.wishlist_name} created by {self.user}'

class WishlistItem(models.Model):
    """
    Model to represent an item added to a wishlist.
    Each item is related to a wishlist and a product.
    """
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='Items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} added to {self.wishlist.wishlist_name}'

