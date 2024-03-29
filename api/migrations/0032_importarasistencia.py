# Generated by Django 5.0.1 on 2024-02-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_delete_importarasistencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportarAsistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idempresa', models.CharField(max_length=6, null=True)),
                ('tipo_envio', models.CharField(max_length=1, null=True)),
                ('idresponsable', models.CharField(max_length=6, null=True)),
                ('idplanilla', models.CharField(max_length=3, null=True)),
                ('idemisor', models.CharField(max_length=3, null=True)),
                ('idturno', models.CharField(max_length=2, null=True)),
                ('fecha', models.CharField(blank=True, max_length=8, null=True)),
                ('idsucursal', models.CharField(max_length=3, null=True)),
                ('item', models.IntegerField(null=True)),
                ('idcodigogeneral', models.CharField(max_length=8, null=True)),
                ('idactividad', models.CharField(max_length=3, null=True)),
                ('idlabor', models.CharField(max_length=6, null=True)),
                ('idconsumidor', models.CharField(max_length=6, null=True)),
                ('cantidad', models.CharField(blank=True, max_length=255)),
                ('idespecie', models.CharField(max_length=3, null=True)),
            ],
        ),
    ]
