# Generated by Django 4.2.2 on 2023-07-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='seller_email',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
