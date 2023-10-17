# Generated by Django 4.2.1 on 2023-09-21 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=255)),
                ('nombres_apellidos', models.CharField(max_length=255)),
                ('servicio', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('titular', models.CharField(max_length=255)),
                ('dpi', models.CharField(max_length=20, unique=True)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('idSector', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('idpredio', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('Vendido', 'Vendido'), ('Disponible', 'Disponible')], default='Disponible', max_length=10)),
                ('dueño', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PagoAgua',
            fields=[
                ('idpagoagua', models.AutoField(primary_key=True, serialize=False)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Multas',
            fields=[
                ('idmultas', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateTimeField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jornales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idJornal', models.PositiveIntegerField(unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.sector')),
            ],
        ),
        migrations.CreateModel(
            name='Fontanero',
            fields=[
                ('idfontanero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('dpi', models.CharField(max_length=20, unique=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('tipo_pago', models.CharField(choices=[('Semanal', 'Semanal'), ('Mensual', 'Mensual'), ('Quincenal', 'Quincenal')], default='Semanal', max_length=10)),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.sector')),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='miusuario',
            name='sector_ubicacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.sector'),
        ),
    ]
