# Generated by Django 3.1.2 on 2020-12-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20201203_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='Bid_Price',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
