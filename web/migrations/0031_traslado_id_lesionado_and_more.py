# Generated by Django 5.1.1 on 2024-09-24 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_tipo_accidente_traslado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='traslado',
            name='id_lesionado',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='web.emergencias_medicas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tipo_accidente',
            name='tipo_accidente',
            field=models.CharField(max_length=40),
        ),
        migrations.CreateModel(
            name='Traslado_Accidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_trasladado', models.CharField(max_length=40)),
                ('medico_receptor', models.CharField(max_length=40)),
                ('mpps_cmt', models.CharField(max_length=20)),
                ('id_lesionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.lesionados')),
            ],
        ),
    ]
