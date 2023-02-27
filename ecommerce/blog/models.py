from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    head0=models.CharField(max_length=100,default="")
    chead0=models.CharField(max_length=5000,default="")
    head1=models.CharField(max_length=100,default="")
    chead1=models.CharField(max_length=5000,default="")
    head2=models.CharField(max_length=100,default="")
    chead2=models.CharField(max_length=5000,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="blog/images",default="")


    def __str__(self):
        return self.title
