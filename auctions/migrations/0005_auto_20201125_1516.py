# Generated by Django 3.1.2 on 2020-11-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201125_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Date_of_Comment',
            field=models.DateTimeField(),
        ),
    ]
