# Generated by Django 5.0.1 on 2024-02-13 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_delete_importarasistencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportarAsistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idempresa', models.CharField(max_length=6, null=True)),
                ('tipo_envio', models.CharField(max_length=1)),
                ('idresponsable', models.CharField(max_length=6)),
                ('idplanilla', models.CharField(max_length=3)),
                ('idemisor', models.CharField(max_length=3)),
                ('idturno', models.CharField(max_length=2)),
                ('fecha', models.CharField(blank=True, max_length=8, null=True)),
                ('idsucursal', models.CharField(max_length=3)),
                ('item', models.IntegerField()),
                ('idcodigogeneral', models.CharField(max_length=8)),
                ('idactividad', models.CharField(max_length=3)),
                ('idlabor', models.CharField(max_length=6)),
                ('idconsumidor', models.CharField(max_length=6)),
                ('cantidad', models.CharField(blank=True, max_length=255)),
                ('idespecie', models.CharField(max_length=3)),
            ],
        ),
    ]
