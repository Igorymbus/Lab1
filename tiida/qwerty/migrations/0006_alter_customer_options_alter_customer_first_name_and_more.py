# Generated by Django 5.2.2 on 2025-06-17 10:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qwerty', '0005_remove_customer_address_remove_customer_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'customer', 'verbose_name_plural': 'customers'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registered_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='registration date'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(blank=True, max_length=100, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_customer',
            field=models.BooleanField(default=False, verbose_name='customer status'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='employee status'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='phone number'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]
