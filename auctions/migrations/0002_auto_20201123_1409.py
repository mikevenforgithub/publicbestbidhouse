# Generated by Django 3.1.2 on 2020-11-23 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Category_of_Listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.categories'),
        ),
    ]