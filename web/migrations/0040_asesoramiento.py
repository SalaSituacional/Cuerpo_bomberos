# Generated by Django 5.1.1 on 2024-09-26 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0039_tipos_traslado_traslado_prehospitalaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesoramiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=12)),
                ('descripcion', models.CharField(max_length=40)),
                ('material_utilizado', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
                ('id_procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos')),
            ],
        ),
    ]
