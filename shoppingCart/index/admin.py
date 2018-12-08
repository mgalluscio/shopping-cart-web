from django.contrib import admin

from  .models import Products, Orders, Order_Items

admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Order_Items)