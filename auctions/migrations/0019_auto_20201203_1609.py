# Generated by Django 3.1.2 on 2020-12-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auto_20201203_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='bid_by',
            field=models.CharField(blank=True, default=0, max_length=25, null=True),
        ),
    ]
