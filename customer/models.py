from django.db import models
from django.contrib.auth.models import User
from owner.models import Books

# Create your models here.

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Books,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    option={
        ("incart","incart"),
        ("cancel","cancel"),
        ("order_placed","order_placed"),

    }
    status=models.CharField(max_length=120,choices=option,default="incart")



class My_orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    address=models.CharField(max_length=250)
    option = {
        ("order_placed", "order_placed"),
        ("Dispatched", "Dispatched"),
        ("cancel", "cancel"),
        ("Intransit", "Intransit"),
        ("delivered", "delivered"),

    }
    status = models.CharField(max_length=120, choices=option, default="order_placed")
    excepted_delivery_date=models.DateField(null=True)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="customer",null=True)
    phone_number=models.CharField(max_length=250)
    address=models.TextField(max_length=250)
    profile_pic=models.ImageField(upload_to="image")


