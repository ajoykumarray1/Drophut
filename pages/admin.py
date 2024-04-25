from django.contrib import admin
from .models import Products_listing


# Register your models here.
@admin.register(Products_listing)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title','product_name','product_price','product_img')