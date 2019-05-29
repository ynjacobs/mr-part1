from django.db import models

class Customer(models.Model):
  email = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  


class Order(models.Model):
  number = models.CharField(max_length=255)
  date = models.TextField(max_length=1000)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name= 'orders')
   







   