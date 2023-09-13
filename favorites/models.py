from django.db import models
from django.contrib.auth import get_user_model

from shop import models as shop_models


class FavoriteProduct(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE, related_name='favorite', verbose_name='Пользователь')
    product = models.ForeignKey(shop_models.Product, models.CASCADE, related_name='favorite', verbose_name='Продукт')

    class Meta:
        verbose_name = 'Израбранный товар'
        verbose_name_plural = 'Избранные товары'
