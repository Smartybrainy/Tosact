# Generated by Django 3.1 on 2020-12-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactenquiries',
            name='granted',
            field=models.BooleanField(default=False),
        ),
    ]
