# Generated by Django 2.2 on 2019-04-28 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20190426_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='session_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
