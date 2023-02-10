# Generated by Django 4.1.6 on 2023-02-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_demomodel_item_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='demomodel',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='demomodel',
            name='code',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='demomodel',
            name='levels',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='demomodel',
            name='units',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='demomodel',
            name='variable_category',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='demomodel',
            name='variable_code',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='demomodel',
            name='variable_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]