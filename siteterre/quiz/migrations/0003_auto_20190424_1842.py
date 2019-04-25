# Generated by Django 2.2 on 2019-04-24 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20190424_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='valid_1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='valid_2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='valid_3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='valid_4',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default='[]', max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice_1',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice_2',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice_3',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice_4',
            field=models.CharField(max_length=300),
        ),
    ]
