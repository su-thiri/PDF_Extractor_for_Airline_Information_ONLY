# Generated by Django 3.2.23 on 2024-01-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update_news', '0002_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='airline_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userdata',
            name='flight_num',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
