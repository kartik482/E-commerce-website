from distutils.command.upload import upload
from email.policy import default
from sqlite3 import Timestamp
from django.db import models
from django.forms import IntegerField

# Create your models here.



class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50)
    price=models.IntegerField(default=00)
    description=models.CharField(max_length=300,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    customer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    subject=models.CharField(max_length=50)
    description=models.CharField(max_length=800,default="")

    def __str__(self):
        return self.name


class Orders(models.Model):


    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=6)
    phone=models.CharField(max_length=16)
    
    

    def __str__(self):
        return self.name


class Order_update(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now=True)

    def __str__(self):
        return self.update_desc[0:7]+"...."








    





# class product(models.Model):
#     contact_id=models.AutoField(primary_key=True,default=0)
#     name=models.CharField(max_length=100,default="")
#     email=models.CharField(max_length=150,default="")
#     phone=models.CharField(max_length=15,default="")
#     desc=models.CharField(max_length=2000,default="")

#     def str(self):
#         return self.name