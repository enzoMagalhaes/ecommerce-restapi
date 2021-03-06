# Generated by Django 3.2 on 2021-12-13 00:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211212_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Celulares', 'celulares'), ('Eletronicos', 'eletronicos'), ('Relogios', 'relogios'), ('Calcados', 'calcados'), ('Bolsas', 'bolsas'), ('Roupas', 'roupas')], default='Eletronicos', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='free_shipping',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='nacional',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount_sold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
