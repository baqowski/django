# Generated by Django 4.0 on 2021-12-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_menucart_products_productorder_prize_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='prize',
        ),
        migrations.AddField(
            model_name='product',
            name='prize',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]