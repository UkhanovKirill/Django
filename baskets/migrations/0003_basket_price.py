# Generated by Django 3.2.12 on 2022-04-14 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0002_basket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
