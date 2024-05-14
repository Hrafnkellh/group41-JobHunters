# Generated by Django 5.0.4 on 2024-05-14 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('profile_image_path', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.CharField(blank=True, max_length=255)),
                ('profile_image_path', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esg_rating', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=255)),
                ('logo_path', models.CharField(blank=True, max_length=255)),
                ('cover_image_path', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
    ]
