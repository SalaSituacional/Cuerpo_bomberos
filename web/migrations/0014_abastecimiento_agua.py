# Generated by Django 5.1.1 on 2024-09-16 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_alter_procedimientos_id_parroquia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abastecimiento_agua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servicio', models.CharField(max_length=40)),
                ('id_procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos')),
            ],
        ),
    ]
