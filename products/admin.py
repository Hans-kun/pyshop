from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "description", "discount")


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


admin.site.register(Product, ProductsAdmin)
admin.site.register(Offer, OfferAdmin)
