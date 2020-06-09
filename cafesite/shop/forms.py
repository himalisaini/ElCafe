from django import forms
from .models import BillingModel


class BillingForm(forms.ModelForm):
        class Meta:
                model = BillingModel
                fields = ('first_name', 'last_name', 'email', 'address', 'phone_number','payment_mode')