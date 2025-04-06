# Generated by Django 5.2 on 2025-04-06 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfermeiro',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.usuario'),
        ),
        migrations.AlterField(
            model_name='farmaceutico',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.usuario'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.usuario'),
        ),
    ]
