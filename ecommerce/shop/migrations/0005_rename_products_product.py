# Generated by Django 4.0.2 on 2022-05-16 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_products_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='product',
        ),
    ]
