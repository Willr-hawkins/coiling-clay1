from django.test import TestCase

from .forms import CreateWishlistForm

class TestCreateWishlistForm(TestCase):
    """ Test create wishlist form for validation. """

    def test_form_is_valid(self):
        """ Test create wishlist form when valid. """
        create_wishlist_form = CreateWishlistForm({
            'wishlist_name': 'Gift Ideas',
            'wishlist_note': 'Potentail gift ideas for friends.'
        })
        self.assertTrue(create_wishlist_form.is_valid(), msg='Create wishlist form is invalid.')

    def test_form_is_invalid(self):
        """ Test create wishlist form when invalid. """
        create_wishlist_form = CreateWishlistForm({
            'wishlist_name': '', #Required
            'wishlist_note': 'Potentail gift ideas for friends.'
        })
        self.assertFalse(create_wishlist_form.is_valid(), msg='Create wishlist form is valid.')