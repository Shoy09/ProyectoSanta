# Generated by Django 5.0.1 on 2024-02-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_planilla'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emisor',
            fields=[
                ('idemisor', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
