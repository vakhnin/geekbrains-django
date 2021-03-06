# Generated by Django 3.2.6 on 2022-06-25 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_short_desc'),
        ('ordersapp', '0002_auto_20220621_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='продукт'),
        ),
    ]
