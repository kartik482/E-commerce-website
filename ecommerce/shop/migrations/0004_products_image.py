# Generated by Django 4.0.2 on 2022-05-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_products_category_products_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
