# Generated by Django 5.1.1 on 2024-12-07 01:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado')], default='pendiente', max_length=20)),
                ('precio_pagado', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to=settings.AUTH_USER_MODEL)),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='viajes.viajes')),
            ],
        ),
    ]
