# Generated by Django 2.2 on 2019-05-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_player_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='explanation',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
