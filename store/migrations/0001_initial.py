# Generated by Django 2.2 on 2019-08-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=400)),
                ('payment_method', models.CharField(max_length=400)),
                ('payment_data', models.CharField(max_length=400)),
                ('items', models.TextField()),
                ('fulfilled', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('imglink', models.CharField(max_length=400)),
            ],
        ),
    ]
