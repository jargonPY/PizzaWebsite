# Generated by Django 2.0.3 on 2019-07-18 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190718_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price_large',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price_one',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price_small',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]