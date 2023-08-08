from . import views
from django.urls import path
app_name="products"
urlpatterns=[
    path("",views.ProductListView.as_view() , name="products") ,
    path("detail/<pk>",views.productDetailView , name="detail")
]