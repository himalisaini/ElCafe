# Generated by Django 2.2.4 on 2020-06-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200610_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingmodel',
            name='final_amount',
            field=models.CharField(default='500', max_length=10),
        ),
        migrations.AlterField(
            model_name='billingmodel',
            name='delivery_time',
            field=models.CharField(default='12:17:56', max_length=20),
        ),
        migrations.AlterField(
            model_name='billingmodel',
            name='order_time',
            field=models.CharField(default='10:17:56', max_length=20),
        ),
    ]