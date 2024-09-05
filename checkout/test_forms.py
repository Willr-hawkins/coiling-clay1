from django.test import TestCase

from .forms import OrderForm


class TestOderForm(TestCase):
    """ Test Order form for validation. """

    def test_form_is_valid(self):
        """ Test order form when valid. """

        order_form = OrderForm({
            'full_name': 'John Doe',
            'email': 'johndoe@test.com',
            'phone_number': '1234567890',
            'street_address1': 'street',
            'street_address2': '',
            'town_or_city': 'anywhere',
            'postcode': '',
            'country': 'GB',
            'county': '',
        })
        self.assertTrue(order_form.is_valid(), msg='Order form is invlaid.')

    def test_form_is_invalid(self):
        """ Test order form when invalid. """

        order_form = OrderForm({
            'full_name': '',  # Required
            'email': '',  # Required
            'phone_number': '',  # Required
            'street_address1': '',  # Required
            'street_address2': 'anywhere',
            'town_or_city': 'anywhere',
            'postcode': '12345',
            'country': '',  # Required
            'county': ' anywhere',
        })
        self.assertFalse(order_form.is_valid(), msg='Order form is vlaid.')
