# Generated by Django 4.2.3 on 2024-03-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='fotos_productos'),
        ),
    ]
