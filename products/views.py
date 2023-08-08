from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import *


# Create your views here.
class ProductListView(ListView):
    template_name = 'products/list.html'
    context_object_name = "products"
    queryset = ProductModel.published.all()



def productDetailView(request, pk):
    product = get_object_or_404(ProductModel, id=pk, status=ProductModel.Status.PUBLISHED)
    context = {
        "product":product
    }
    return render(request, "products/detail.html", context)
