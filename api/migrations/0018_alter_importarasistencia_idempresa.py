# Generated by Django 5.0.1 on 2024-02-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_importarasistencia_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importarasistencia',
            name='idempresa',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
