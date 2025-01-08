# Generated by Django 5.1.1 on 2024-12-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Installed_capacity', models.CharField(max_length=100)),
                ('Energy_generated', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Size', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Load', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default='Online', max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('Commissioned', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('normal', 'Normal'), ('warning', 'Warning'), ('alarm', 'Alarm')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'System Statuses',
            },
        ),
    ]
