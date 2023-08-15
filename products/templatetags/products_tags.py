from django import template
from ..models import *
from  django.db.models import Count
register = template.Library()


@register.simple_tag
def most_popular_products(count=5):
    return ProductModel.published.annotate(comments_count=Count('comments')).order_by('-comments')[:count]
@register.inclusion_tag("partials/latest_products.html")
def latest_products(count=5):
    l_products = ProductModel.published.order_by("-publish")[:count]
    context = {
        "l_products": l_products
    }
    return context














