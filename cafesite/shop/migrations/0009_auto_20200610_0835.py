# Generated by Django 2.2.4 on 2020-06-10 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0008_auto_20200610_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingmodel',
            name='customer',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='billingmodel',
            name='delivery_time',
            field=models.CharField(default='10:35:42', max_length=20),
        ),
        migrations.AlterField(
            model_name='billingmodel',
            name='order_time',
            field=models.CharField(default='08:35:42', max_length=20),
        ),
    ]
