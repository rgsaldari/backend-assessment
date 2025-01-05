# Generated by Django 5.1.4 on 2025-01-05 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short', models.CharField(default=None, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.CharField(default=None, max_length=5, primary_key=True, serialize=False)),
                ('departure_airport', models.CharField(max_length=3)),
                ('arrival_airport', models.CharField(max_length=3)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('stops', models.IntegerField()),
                ('duration_mins', models.IntegerField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.airline')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.CharField(default=None, max_length=10, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agent')),
                ('legs', models.ManyToManyField(related_name='legs', to='api.leg')),
            ],
        ),
    ]