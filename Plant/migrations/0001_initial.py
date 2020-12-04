# Generated by Django 3.1.3 on 2020-12-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('g_sunlight', models.IntegerField()),
                ('water', models.IntegerField()),
                ('g_temp', models.IntegerField()),
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('h_sunlight', models.IntegerField()),
                ('h_temp', models.IntegerField()),
                ('desired_size', models.CharField(max_length=1)),
            ],
        ),
    ]
