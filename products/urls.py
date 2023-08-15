from . import views
from django.urls import path
app_name="products"
urlpatterns=[
    path("", views.index, name="index"),
    path("list",views.ProductListView.as_view() , name="products") ,
    path("products/<pk>",views.productDetailView , name="detail"),
    path("contact",views.contactView ,name="contact" ),
    # path("products/<product_id>/comment",views.product_comment,name="comments_id")
    path("products/<product_id>/comment",views.product_comment,name="comments_id")
]