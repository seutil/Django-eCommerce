from django.db import models
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import get_user_model

from shop import models as shop_models


class Cart(auth_mixins.LoginRequiredMixin, models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE, related_name='cart', verbose_name='Пользователь')
    product = models.ForeignKey(shop_models.Product, models.CASCADE, related_name='cart', verbose_name='Продукт')

    class Meta:
        verbose_name = 'Корзина пользователя'
        verbose_name_plural = 'Корзины пользователей'
