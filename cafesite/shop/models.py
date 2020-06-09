from django.db import models
from datetime import datetime , timedelta


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

    def __str__(self):
        return self.first_name




