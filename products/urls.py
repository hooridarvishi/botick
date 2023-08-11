from . import views
from django.urls import path
app_name="products"
urlpatterns=[
    path("", views.index, name="index"),
    path("list",views.ProductListView.as_view() , name="products") ,
    path("detail/<pk>",views.productDetailView , name="detail"),
    path("contact",views.Contact_us ,name="contact" )
]