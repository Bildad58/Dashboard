# Generated by Django 5.1.1 on 2024-12-18 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VictronCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Victron Credentials',
            },
        ),
        migrations.CreateModel(
            name='VictronSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installation_id', models.CharField(max_length=100)),
                ('last_sync', models.DateTimeField(auto_now=True)),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.sites')),
            ],
        ),
    ]
