# Generated by Django 2.1.2 on 2018-11-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.FloatField()),
                ('product_size', models.CharField(max_length=20)),
                ('product_description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterField(
            model_name='customers',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
