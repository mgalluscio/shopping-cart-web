# Generated by Django 2.1.2 on 2018-11-30 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20181128_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='items',
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Orders'),
        ),
    ]
