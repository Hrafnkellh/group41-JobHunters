# Generated by Django 5.0.4 on 2024-05-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]