# Generated by Django 3.1.2 on 2020-11-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201125_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Date_of_Comment',
            field=models.DateField(),
        ),
    ]
