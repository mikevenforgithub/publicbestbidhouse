# Generated by Django 3.1.2 on 2020-12-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20201203_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='Bid_Price',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
