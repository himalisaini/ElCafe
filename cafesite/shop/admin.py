from django.contrib import admin
from . models import Item , BillingModel , Review
# Register your models here.

admin.site.register(Item)
admin.site.register(BillingModel)
admin.site.register(Review)