# Generated by Django 5.1.3 on 2024-12-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_brand_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Availability',
            field=models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=1000, null=True),
        ),
    ]
