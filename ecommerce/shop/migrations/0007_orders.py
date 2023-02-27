# Generated by Django 4.0.2 on 2022-06-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=6)),
            ],
        ),
    ]
