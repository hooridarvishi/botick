from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import *
from .forms import *
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import TrigramSimilarity
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "products/index.html")


def ProductListView(request, category=None):
    if category is not None:
        products = ProductModel.published.filter(category=category)
    else:
        products = ProductModel.objects.all()

    context = {
        'products': products,
        "category": category
    }
    return render(request, "products/list.html", context)


# class ProductListView(ListView):
#     template_name = 'products/list.html'
#     context_object_name = "products"
#     queryset = ProductModel.published.all()
#     paginate_by = 6


def productDetailView(request, pk):
    # global comment
    product = get_object_or_404(ProductModel, id=pk, status=ProductModel.Status.PUBLISHED)
    # comments = product.comments.filter(active=True)
    # form = CommentForm()
    # if request.method=="POST":
    #     print(request)
    #     form=CommentForm(data=request.POST)
    #     print("***")
    # comment=None
    # if form.is_valid():
    #     print("is valid+++")
    # comment=form.save(commit=False)
    # comment.product=product
    # comment.save()
    # cd = form.cleaned_data
    # CommentModel.objects.create(
    #     title=cd["title"],
    #     message_positive_points=cd["message_positive_points"],
    #     message_negative_points=cd["message_negative_points"], message_text=cd["message_text"]
    # )
    # return redirect("products:index")
    # else:
    #     form=CommentForm()
    context = {
        "product": product,
        # "comments": comments,
        # "form": form ,
        # "comment":comment
    }
    return render(request, "products/detail.html", context)


def commentView(request):
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            CommentModel.oblects.create(message_positive_points=cd["message_positive_points"],
                                        message_negative_points=cd["message_negative_points"],
                                        message_text=cd["message_text"]
                                        )
            return redirect("products:index")
    else:
        form = CommentForm()
    return render(request, "products/detail.html", {"form": form})


def contactView(request):
    if request.method == "POST":
        form = Contact_us(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactModel.objects.create(email=cd['email'], body=cd['body'], name=cd['name'])

            return redirect("products:index")
    else:
        form = Contact_us()
    return render(request, "forms/contact_us.html", {"form": form})


#
# @require_POST
# def product_comment(request, product_id):
#     product = get_object_or_404(ProductModel, id=product_id, status=ProductModel.Status.PUBLISHED)
#     # comment = None
#     form = CommentForm(data=request.POST)
#     if form.is_valid():
#         cd=form.cleaned_data
#         CommentModel.objects.create(
#             title=cd["title"] , message_positive_points=cd["message_positive_points"] ,
#             message_negative_points=cd["message_negative_points"] , message_text=cd["message_text"]
#         )
#         return redirect("products:index")
#     else:
#         form=CommentForm()
#     context = {
#         "product": product,
#         "form": form
#     }
#     return render(request, "forms/comment.html", context)


def search_products_view(request):
    query = None
    results = []
    if "query" in request.GET:
        print("#")
        print(query)
        form = SearchProduct(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            result1 = ProductModel.published.annotate(similarity=TrigramSimilarity("title", query)).filter(
                similarity__gt=0.1)
            print("****")
            print(result1)
            result2 = ProductModel.published.annotate(similarity=TrigramSimilarity("description", query)).filter(
                similarity__gt=0.1)
            print(result2)
            results = (result1 | result2).order_by("-similarity")
            print(results)
    context = {
        "query": query,
        "results": results
    }
    return render(request, "products/search.html", context)


# @require_POST
# def contact_result_view(request):
#     message = None
#     form = Contact_us(request.POST)
#     print(request.POST)
#     if form.is_valid():
#         message = form.save()
#         # message.save()
#     context = {

#         "message": message,
#         "form": form,
#     }
#     return render(request, "forms/contact_result.html", context)
@login_required
def profile(request):
    user_ = User.objects.all
    user = request.user
    save_products=user.saved_posts.all()
    products = ProductModel.published.filter(author=user)
    return render(request, "products/profile.html", {"products": products, "user": user, "user_": user_ ,"save_products":save_products})


@login_required
def create_products(request):
    if request.method == "POST":
        form = CreateProductsForm(request.POST, request.FILES)
        if form.is_valid:
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            ImageModel.objects.create(image_file=form.cleaned_data["image1"], product=product)
            ImageModel.objects.create(image_file=form.cleaned_data["image2"], product=product)
    else:
        form = CreateProductsForm()
    return render(request, "forms/create_product.html", {"form": form})


@login_required
def delete_products(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("products:profile")
    return render(request, "forms/delete_products.html", {"product": product})


@login_required
def edit_products(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    if request.method == "POST":
        form = CreateProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            ImageModel.objects.create(image_file=form.cleaned_data["image1"], product=product)
            ImageModel.objects.create(image_file=form.cleaned_data["image2"], product=product)
            return redirect("products:profile")
    else:
        form = CreateProductsForm(instance=product)
    return render(request, "forms/create_product.html", {"form": form, "product": product})


@login_required
def delete_image(request, image_id):
    image = get_object_or_404(ImageModel, id=image_id)
    image.delete()
    return redirect("products:profile")


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("products:profile")
                else:
                    return HttpResponse("کاربر اکتیو نیستی")
            else:
                return HttpResponse("شما در لیست کاربران نیستی ابتدا ثبت نام کن")
    else:
        form = LoginForm()
    return render(request, "forms/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Account.objects.create(user=user)
            return render(request, "registration/register_done.html", {"user": user})

    else:
        form = UserRegisterForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def edit_account(request):
    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=request.user)
        account_form = EditAccountForm(request.POST, instance=request.user.account, files=request.FILES)
        if account_form.is_valid() and user_form.is_valid():
            account_form.save()
            user_form.save()
    else:
        user_form = EditUserForm(instance=request.user)
        account_form = EditAccountForm(instance=request.user.account)
    context = {
        "user_form": user_form,
        "account_form": account_form
    }

    return render(request, "registration/edit_account.html", context)


@login_required
@require_POST
def like_product(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        product = get_object_or_404(ProductModel, id=product_id)
        user = request.user
        if user in product.likes.all():
            product.likes.remove(user)
            print("unliked")
            liked = False
            print("unliked _")
        else:
            product.likes.add(user)
            print("liked")
            liked = True
            print("liked +")
        product_likes_count = product.likes.count()
        print(product_likes_count)
        response_data = {
            'liked': liked,
            'likes_count': product_likes_count
        }
    else:
        response_data = {
            "error": "invalid product_id"
        }
    return JsonResponse(response_data)

def save_product(request):

    product_id = request.POST.get("product_id")
    if product_id is not None:
        product = ProductModel.objects.get(pk=product_id)
        user = request.user
        if user in product.saved_by.all():
            product.saved_by.remove(user)
            saved = False
        else:
            product.saved_by.add(user)
            saved = True
        return JsonResponse({"saved":saved})


    return JsonResponse({"error":"invalid request"})



