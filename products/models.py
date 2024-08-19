from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    
    def __str__(self):
        return self.name

class Review(models.Model):
    """ A model to leave reviews on products. """

    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators = [
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    review_body = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-review_date']

    def __str__(self):
        return f"Review by {self.reviewer}"
