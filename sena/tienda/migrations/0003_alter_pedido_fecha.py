# Generated by Django 3.2.12 on 2024-01-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(),
        ),
    ]