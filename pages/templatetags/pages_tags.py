from django import template

from favorites import models as favorites_models
from cart import models as cart_models

register = template.Library()


@register.inclusion_tag('tags/product_card.html')
def get_product_card(product, width):
    return {
        'product': product,
        'width': width,
        'favorite': favorites_models.FavoriteProduct.objects.filter(product=product),
        'in_cart': cart_models.Cart.objects.filter(product=product),
    }