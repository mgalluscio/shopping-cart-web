from django.contrib import admin

from  .models import Customers, Products, Orders, Order_Items

admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Order_Items)