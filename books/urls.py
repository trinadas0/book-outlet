from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/update/<int:book_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/delete/<int:book_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's auth URLs
]
