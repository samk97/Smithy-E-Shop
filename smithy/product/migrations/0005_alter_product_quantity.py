# Generated by Django 4.2.2 on 2023-07-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_category_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]