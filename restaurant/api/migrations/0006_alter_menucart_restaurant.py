# Generated by Django 4.0 on 2021-12-15 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_menucart_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucart',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuCarts', to='api.restaurant'),
        ),
    ]
