from django import template
from ..models import *

register = template.Library()


# @register.simple_tag
# def most_popular_products(count=5):
#     return ProductModel.published.annotate()
@register.inclusion_tag("partials/latest_products.html")
def latest_products(count=5):
    l_products = ProductModel.published.order_by("-publish")[:count]
    context = {
        "l_products": l_products
    }
    return context














