from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from . import models
from shop import models as shop_models


class AddToCartView(auth_mixins.LoginRequiredMixin, views.View):

    def post(self, request, product_pk):
        models.Cart.objects.create(
            user=request.user,
            product=shop_models.Product.objects.get(pk=product_pk),
        )
        return redirect(reverse('cart'))


class DeleteFromCartView(auth_mixins.LoginRequiredMixin, views.View):

    def post(self, request, product_pk):
        models.Cart.objects.filter(
            user=request.user,
            product=shop_models.Product.objects.get(pk=product_pk),
        ).delete()
        return redirect(reverse('cart'))


class ClearCartView(auth_mixins.LoginRequiredMixin, views.View):

    def post(self, request):
        models.Cart.objects.delete()
        return redirect(reverse('cart'))


class CartView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = models.Cart
    context_object_name = 'cart'
