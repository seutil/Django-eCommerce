from django.urls import path

from . import views


urlpatterns = [
    path('clear/', views.ClearCartView.as_view(), name='clear_cart'),
    path('add/<int:product_pk>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('delete/<int:product_pk>/', views.DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('', views.CartView.as_view(), name='cart'),
]
