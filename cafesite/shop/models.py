from django.db import models
from datetime import datetime , timedelta
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'],name='check_unique'),
        ]


def get_date():
    x = datetime.now()
    return x.strftime("%x")


def get_time():
    x = datetime.now()
    y = x + timedelta(hours=2)
    return y.strftime("%X")


class BillingModel(models.Model):
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200,blank=False)
    phone_number = models.CharField(max_length=10,blank=False)
    address = models.TextField(default='Enter your address here..')
    payment_mode = models.CharField(max_length=20)
    order_date = models.CharField(default=get_date(),max_length=50)
    order_time = models.CharField(default=datetime.now().strftime("%X"),max_length=20)
    delivery_time = models.CharField(default=get_time(),max_length=20)
    cart_items = models.TextField(default='Yummy dishes here!')
    item_quantity = models.CharField(max_length=500,default='Item quantity')
    item_price = models.CharField(max_length=500,default='Item price')
    item_disc = models.CharField(max_length=500,default='Discount applied')
    total_price = models.CharField(max_length=10,default='1000')
    discount_applied = models.CharField(max_length=10,default='500')
    final_amount = models.CharField(max_length=10, default='500')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order {self.pk} {self.first_name}'

    def get_absolute_url(self):
        return reverse('order_details', kwargs={'id': self.pk})


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.CharField(default=get_date(),max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} review'

    def get_absolute_url(self):
        return reverse('review-detail',kwargs={'pk':self.pk})






