from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import *
from .forms import *
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    return render(request, "products/index.html")


class ProductListView(ListView):
    template_name = 'products/list.html'
    context_object_name = "products"
    queryset = ProductModel.published.all()
    paginate_by = 6


def productDetailView(request, pk):
    product = get_object_or_404(ProductModel, id=pk, status=ProductModel.Status.PUBLISHED)
    comments = product.comments.filter(active=True)
    form = CommentForm()
    context = {
        "product": product,
        "comments": comments,
        "form": form
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


@require_POST
def product_comment(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id, status=ProductModel.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.save()
    context = {
        "product": product,
        "comment": comment,
        "form": form
    }
    return render(request, "forms/comment.html", context)
