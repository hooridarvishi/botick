from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, "products/index.html")


class ProductListView(ListView):
    template_name = 'products/list.html'
    context_object_name = "products"
    queryset = ProductModel.published.all()


def productDetailView(request, pk):
    product = get_object_or_404(ProductModel, id=pk, status=ProductModel.Status.PUBLISHED)
    context = {
        "product": product
    }
    return render(request, "products/detail.html", context)


def contactView(request):
    if request.method == "POST":
        form = Contact_us(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactModel.objects.create(message=cd['message'], name=cd['name'], email=cd['email'],
                                        phone=cd['phone'], subject=cd['subject'])

            return redirect("products:index")
    else:
        form = Contact_us()

    return render(request, "forms/contact_us.html", {"form": form})
