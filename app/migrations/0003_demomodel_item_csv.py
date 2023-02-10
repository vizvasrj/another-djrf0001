# Generated by Django 4.1.6 on 2023-02-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('levels', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=256)),
                ('units', models.CharField(max_length=256)),
                ('variable_code', models.CharField(max_length=256)),
                ('variable_name', models.CharField(max_length=256)),
                ('variable_category', models.CharField(max_length=256)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='csv',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
