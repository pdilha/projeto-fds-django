# Generated by Django 5.1.6 on 2025-04-06 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=models.DateField(),
        ),
    ]
