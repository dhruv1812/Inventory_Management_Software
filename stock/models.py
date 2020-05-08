from django.db import models

# Create your models here.

class products(models.Model):

    product_id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=100)
    count_inventory = models.IntegerField()
    count_sold = models.IntegerField()






class customers(models.Model):

    customer_id = models.CharField(max_length=100,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)



class orders(models.Model):

    order_id = models.CharField(max_length=100,primary_key=True)
    product_id = models.ForeignKey('products',on_delete=models.CASCADE)
    customer_id = models.ForeignKey('customers',on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
