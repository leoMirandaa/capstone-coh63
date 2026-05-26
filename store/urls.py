from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductList.as_view(), name="catalog"),
    path("add_to_cart", views.add_to_cart, name="cart_add"),
    path("cart", views.cart, name="cart"),
]
