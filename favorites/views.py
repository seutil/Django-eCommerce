from django.views import generic as views
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import mixins as auth_mixins

from . import models
from shop import models as shop_models 


class AddFavoriteView(auth_mixins.LoginRequiredMixin, views.View):

    def post(self, request, product_pk):
        models.FavoriteProduct.objects.create(
            user=request.user,
            product=shop_models.Product.objects.get(pk=product_pk),
        )
        return redirect(reverse('products'))


class DeleteFavoriteView(auth_mixins.LoginRequiredMixin, views.View):

    def post(self, request, product_pk):
        models.FavoriteProduct.objects.filter(
            user=request.user,
            product=shop_models.Product.objects.get(pk=product_pk),
        ).delete()
        return redirect(reverse('favorites'))


class FavoriteProductsView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = models.FavoriteProduct
    template_name = 'favorite/favorite_list.html'
    context_object_name = 'favorite_products'

    def get_queryset(self):
        return models.FavoriteProduct.objects.filter(user=self.request.user)
