# Generated by Django 5.0.1 on 2024-02-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='idturno',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]
