from django.db import models


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
