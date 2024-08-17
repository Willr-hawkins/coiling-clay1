from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """ A form for users to fill out to leave a review. """
    class Meta:
        model = Review
        fields = ('rating', 'review_body')
