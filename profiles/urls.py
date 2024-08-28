from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('wishlists/', views.user_wishlists, name='wishlists'),
    path('wishlists/create', views.create_wishlist, name='create_wishlist'),
]