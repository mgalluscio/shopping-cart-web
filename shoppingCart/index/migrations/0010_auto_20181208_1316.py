# Generated by Django 2.1.3 on 2018-12-08 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20181129_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order_items',
            name='is_ordered',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='is_ordered',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_description',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_size',
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
    ]
