# Generated by Django 4.2.13 on 2024-07-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subcatid', models.AutoField(primary_key=True, serialize=False)),
                ('catname', models.CharField(max_length=50)),
                ('subcatname', models.CharField(max_length=50, unique=True)),
                ('subcaticonname', models.CharField(max_length=100)),
            ],
        ),
    ]