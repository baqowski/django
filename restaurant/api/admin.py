from django.contrib import admin

from .models import Restaurant, MenuCart, Product, ProductOrder, Order

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(MenuCart)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductOrder)


