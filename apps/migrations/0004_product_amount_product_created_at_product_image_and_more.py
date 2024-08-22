# Generated by Django 5.0.6 on 2024-08-17 12:57

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_cart_remove_product_amount_remove_product_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default=1, force_format=None, keep_meta=True, quality=-1, scale=None, size=[1000, 800], upload_to='products/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
