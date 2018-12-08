from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_image = models.FileField()
    class Meta:
        verbose_name_plural = "Products"
    def __str__(self):
        return self.product_name
    
class Orders(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Orders"
    def __str__(self):
        return str(self.id)

class Order_Items(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Order Items"
    def __str__(self):
        return self.product_id.product_name
    


    







