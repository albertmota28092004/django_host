# Generated by Django 3.2.12 on 2024-03-04 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, default='fotos/default.png', null=True, upload_to='fotos')),
                ('nombre', models.CharField(max_length=254)),
                ('apellido', models.CharField(max_length=254)),
                ('nick', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('rol', models.IntegerField(choices=[(1, 'Administrador'), (2, 'Empleado'), (3, 'Usuario')], default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Enviado'), (3, 'Rechazado')], default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('precio', models.IntegerField()),
                ('fecha_compra', models.DateField()),
                ('stock', models.IntegerField(default=1)),
                ('foto', models.ImageField(blank=True, default='fotos_productos/default.png', null=True, upload_to='fotos_productos')),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_historico', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_hora', models.DateTimeField(max_length=254)),
                ('precio', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.usuario')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicio')),
            ],
        ),
    ]
