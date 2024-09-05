from django.test import TestCase

from .forms import ProductForm, ReviewForm, CommentForm
from .models import Category


class TestProductForm(TestCase):
    """ Test the product form for validation. """
    def test_form_is_valid(self):
        """ Test the Product form when valid. """
        category = Category.objects.create(name='Mugs', friendly_name='Mugs')

        product_form = ProductForm({
            'category': category.id,
            'sku': 'pp10',
            'name': 'Blue mug',
            'description': 'This is a blue mug',
            'price': 10.00,
            'image_url': '',
            'image': '',
        })
        print(product_form.errors)
        self.assertTrue(product_form.is_valid(),
                        msg='Product form is invalid.')

    def test_form_is_invalid(self):
        """ Test the Product form when invalid. """
        product_form = ProductForm({
            'category': '',
            'sku': 'pp10',
            'name': '',
            'description': 'This is a blue mug',
            'price': 10.00,
            'image_url': '',
            'image': '',
        })
        self.assertFalse(product_form.is_valid(), msg='Product form is valid.')


class TestReviewForm(TestCase):
    """ Test the review form for validation. """

    def test_form_is_valid(self):
        """ Test the review form when valid """
        review_form = ReviewForm({
            'rating': 3,
            'review_body': 'I love this mug',
        })
        self.assertTrue(review_form.is_valid(), msg='Review form is invalid.')

    def test_form_is_invalid(self):
        """ Test the review form when invalid """
        review_form = ReviewForm({
            'rating': 3,
            'review_body': '',
        })
        self.assertFalse(review_form.is_valid(), msg='Review form is valid.')


class TestCommentForm(TestCase):
    """ Test the comment form for validation. """

    def test_form_is_valid(self):
        """ Test the comment form when valid. """
        comment_form = CommentForm({
            'comment_body': 'I also love this mug.',
        })
        self.assertTrue(comment_form.is_valid(),
                        msg='Comment form is invalid.')

    def test_form_is_invalid(self):
        """ Test the comment form when invalid. """
        comment_form = CommentForm({
            'comment_body': '',
        })
        self.assertFalse(comment_form.is_valid(), msg='Comment form is valid.')
