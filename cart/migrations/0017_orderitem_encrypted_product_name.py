# Generated by Django 4.2.1 on 2023-08-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0016_alter_orderitem_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="encrypted_product_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]