# Generated by Django 4.2.1 on 2023-08-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0015_alter_orderitem_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
