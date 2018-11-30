from django.db import models
from django.contrib.auth.models import User

    
class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    telephone = models.CharField(max_length=11)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=3)
    zip_code = models.CharField(max_length=5)
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    class Meta:
        verbose_name_plural = "Customers"

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_size = models.CharField(max_length=20)
    product_description = models.CharField(max_length=50) 
    product_image = models.FileField()
    class Meta:
        verbose_name_plural = "Products"
    def __str__(self):
        return self.product_name
    

class Orders(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Orders"
    def __str__(self):
        return str(self.id)

class Order_Items(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    is_ordered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Order Items"
    def __str__(self):
        return self.product_id.product_name
    







