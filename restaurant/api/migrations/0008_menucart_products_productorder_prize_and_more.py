# Generated by Django 4.0 on 2021-12-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_pricelistproduct_pricelist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menucart',
            name='products',
            field=models.ManyToManyField(to='api.Product'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='prize',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]