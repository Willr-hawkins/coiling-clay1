from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from products.models import Product


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


