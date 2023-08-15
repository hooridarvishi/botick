from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status', "price"]
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
    list_display = ['name','product', 'active']
@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email']