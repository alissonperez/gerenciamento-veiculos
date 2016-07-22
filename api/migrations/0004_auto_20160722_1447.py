# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_vehiclemodel_model_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodel',
            name='model_type',
            field=models.CharField(choices=[('car', 'Carro'), ('motorcycle', 'Moto')], default='car', max_length=20),
        ),
    ]
