# Generated by Django 3.2.12 on 2024-02-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_alter_pedido_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='argenisgaray28@gmail.com', max_length=254),
        ),
    ]