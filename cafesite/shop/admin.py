from django.contrib import admin
from . models import Item , BillingModel
# Register your models here.

admin.site.register(Item)
admin.site.register(BillingModel)