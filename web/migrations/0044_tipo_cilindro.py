# Generated by Django 5.1.1 on 2024-10-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0043_retencion_preventiva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Cilindro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cilindro', models.CharField(max_length=50)),
            ],
        ),
    ]
