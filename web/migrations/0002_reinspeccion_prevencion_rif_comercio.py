# Generated by Django 5.1.1 on 2024-10-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reinspeccion_prevencion',
            name='rif_comercio',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
