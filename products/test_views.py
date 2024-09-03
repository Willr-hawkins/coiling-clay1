from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages

from .models import Product, Category, Review
from.forms import ReviewForm, CommentForm


class TestAllProductView(TestCase):
    """ Testing the all_products view. """

    def setUp(self):
        """ Create mock data for testing. """

        self.category1 = Category.objects.create(name='Mugs')
        self.category2 = Category.objects.create(name='vases')

        self.product1 = Product.objects.create(
            name='Blue Mug', description='A ncie blue mug.', price=12.50, category=self.category1
        )
        self.product2 = Product.objects.create(
            name='Red Vase', description='A nice red vase.', price=28.00, category=self.category2
        )

    def test_render_products_page(self):
        """ Test the rendering of the default products page. """

        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(len(response.context['products']), 2)

class TestProductDetailView(TestCase):
    """ Test the product_detail view. """

    def setUp(self):
        """ Create mock data for testing. """

        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.category = Category.objects.create(name='Mugs')

        self.product = Product.objects.create(
            name='Blue Mug', description='A ncie blue mug.', price=12.50, category=self.category
        )
        self.related_product = Product.objects.create(
            name='Red Mug', description='A ncie red mug.', price=12.50, category=self.category
        )
        self.review = Review.objects.create(
            product=self.product, rating=4, reviewer=self.user, review_body='A very nice mug!' 
        )

    def test_product_detail_view(self):
        """ Test rendering the product detail page. """
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.context['product'], self.product)
        self.assertIn('reviews', response.context)
        self.assertEqual(len(response.context['reviews']), 1)
        self.assertIsInstance(response.context['review_form'], ReviewForm)
        self.assertIsInstance(response.context['comment_form'], CommentForm)
        self.assertIn(self.related_product, response.context['random_related_products'])