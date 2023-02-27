import django
from django.contrib import admin

# Register your models here.
from .models import Contact, Order_update, Orders, product
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(Order_update)