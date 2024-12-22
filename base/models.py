from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300,default='username')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Occupied', 'Occupied')])

class Category(models.Model):
    name = models.CharField(max_length=100)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Waiter(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=15)

class Reception(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=15)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

