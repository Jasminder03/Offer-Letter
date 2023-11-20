from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime,date
from django.contrib.admin.widgets import AdminSplitDateTime
from django.core.validators import MaxLengthValidator
'name','address','zip_code','email_address','phone,ref_id','registered_on'


class registration(models.Model):
    ref_id = models.CharField('Reference No.',default = uuid.uuid4, max_length=8 )
    name = models.CharField('Name', max_length=30)
    address = models.CharField('Address', max_length=60)
    phone = models.CharField('Phone', max_length=10)
    zip_code = models.CharField('Zip Code', max_length= 6)
    email_address = models.EmailField('Email Address', max_length=40)
    registered_on = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    
    def __str__(self):
        return self.ref_id
    

class Image(models.Model):
    image_caption = models.CharField(max_length=8)
    image = models.ImageField(upload_to="images/", null= True, )

    def __str___(self):
        return self.image_caption


class Image2(models.Model):
    image_caption = models.CharField(max_length=8)
    image = models.ImageField(upload_to="images/", null= True, )

    def __str___(self):
        return self.image_caption
    


   