# Generated by Django 3.2.23 on 2024-02-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update_news', '0005_userdata_passport_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='eticket',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
