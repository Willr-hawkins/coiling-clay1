from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('wishlists/', views.user_wishlists, name='wishlists'),
    path('wishlists/create', views.create_wishlist, name='create_wishlist'),
    path('wishlists/delete<int:wishlist_id>',
         views.delete_wishlist,
         name='delete_wishlist'),
    path('wishlists/<int:wishlist_id>/',
         views.wishlist_details,
         name='wishlist_details'),
    path('wishlist/add/<int:product_id>/<int:wishlist_id>/',
         views.add_to_wishlist,
         name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_id>/<int:product_id>/',
         views.remove_from_wishlist,
         name='remove_from_wishlist'),
]
