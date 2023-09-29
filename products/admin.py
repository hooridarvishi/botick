from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin
from django.contrib.auth.admin import UserAdmin
admin.sites.AdminSite.site_header = "پنل مدیریت جنگو"
admin.sites.AdminSite.site_title = "پنل  "
admin.sites.AdminSite.index_title = "پنل مدیریت "


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status', "price","old_price","discount"]
    ordering = ['title', 'publish']
    list_filter = ['status', ('publish', JDateFieldListFilter), 'author']
    search_fields = ['title', 'description']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {"slug": ['title']}
    list_editable = ['status']


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'created', 'title']


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = [ 'product', 'active',"message_positive_points"]


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['body', 'email']

@admin.register(User)
class Account(UserAdmin):
    list_display=["username","first_name","last_name","phone"]
    fieldsets=UserAdmin.fieldsets + (
        ("additional information",{"fields":("date_of_birth","bio","photo","job","phone")}),
    )