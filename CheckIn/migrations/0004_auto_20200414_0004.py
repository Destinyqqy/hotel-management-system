# Generated by Django 3.0.4 on 2020-04-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CheckIn', '0003_preferred_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.CharField(choices=[(1, '男'), (0, '女')], max_length=10),
        ),
        migrations.AlterField(
            model_name='past_customer',
            name='sex',
            field=models.CharField(choices=[(1, '男'), (0, '女')], max_length=10),
        ),
    ]
