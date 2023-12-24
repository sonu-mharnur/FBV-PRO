# Generated by Django 4.1.6 on 2023-12-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('discount', models.CharField(max_length=40)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
