# Generated by Django 3.1.2 on 2020-12-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20201130_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='Bid_Price',
            field=models.IntegerField(),
        ),
    ]