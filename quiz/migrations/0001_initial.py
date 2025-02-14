# Generated by Django 2.2 on 2019-04-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('group', models.IntegerField(db_index=True)),
                ('score', models.IntegerField(default=0)),
                ('lives', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=300)),
                ('choice_1', models.CharField(max_length=300)),
                ('choice_2', models.CharField(max_length=300)),
                ('choice_3', models.CharField(max_length=300)),
                ('choice_4', models.CharField(max_length=300)),
                ('answer', models.CharField(default='[]', max_length=500)),
            ],
        ),
    ]
