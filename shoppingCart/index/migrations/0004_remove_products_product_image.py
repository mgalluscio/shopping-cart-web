# Generated by Django 2.1.2 on 2018-11-26 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_products_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_image',
        ),
    ]
