from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('wishlists/', views.user_wishlists, name='wishlists'),
    path('wishlists/create', views.create_wishlist, name='create_wishlist'),
    path('wishlists/<int:wishlist_id>/', views.wishlist_details, name='wishlist_details'),
    path('wishlist/add/<int:product_id>/<int:wishlist_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]