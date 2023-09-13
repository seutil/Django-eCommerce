from django.urls import path

from . import views


urlpatterns = [
    path('add/<int:product_pk>/', views.AddFavoriteView.as_view(), name='add_favorite'),
    path('delete/<int:product_pk>/', views.DeleteFavoriteView.as_view(), name='delete_favorite'),
    path('', views.FavoriteProductsView.as_view(), name='favorites'),
]
