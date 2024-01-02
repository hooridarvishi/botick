from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
app_name="products"
urlpatterns=[
    path("", views.index, name="index"),
    path("list/", views.ProductListView, name="products"),
    path("list/<str:category>",views.ProductListView , name="products_category") ,
    path("products/<pk>",views.productDetailView , name="detail"),
    path("contact",views.contactView ,name="contact" ),
    # path("products/<product_id>/comment",views.product_comment,name="comments_id"),
    path("search/",views.search_products_view,name="search"),
    path("profile/",views.profile,name="profile"),
    path("profile/create_products/",views.create_products , name="create_products"),
    path("profile/delete_products/<product_id>",views.delete_products,name="delete_products"),
    path("profile/delete_image/<image_id>",views.delete_image, name="delete_image"),
    path("profile/create_product/<image_id>", views.edit_products, name="edit_products"),
    path("login/",views.login_user , name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("password_change/",auth_views.PasswordChangeView.as_view(success_url="done"),name="password_change"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path("password-reset/",auth_views.PasswordResetView.as_view(success_url="done"),name="password-reset"),
    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(success_url="/products/password-reset/complete"),name="password_reset_confirm"),
    path("password-reset/complete",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path("register/",views.register,name="register"),
    path("account/edit",views.edit_account , name="edit_account"),
    path("like_product/" , views.like_product , name="like_product"),
    path("save_product/", views.save_product, name="save_product"),
]