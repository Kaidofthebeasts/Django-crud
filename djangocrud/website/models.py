from django.db import models

# Create your models here.

class Customer(models.Model):
  join_date = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField(max_length=100)
  last_name =models.CharField(max_length=100)
  email=models.CharField(max_length=100)
  phone= models.CharField(max_length=15)
  address =models.CharField(max_length=100)
  city=models.CharField(max_length=100)
  
  def __str__(self) -> str:
    return (f"{self.first_name} {self.last_name}")

class Product(models.Model):
  product_name=models.CharField(max_length=50)
  description=models.TextField(null=True)
  price = models.FloatField()
  image = models.ImageField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
        return self.product_name