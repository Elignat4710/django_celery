# Generated by Django 3.0 on 2019-12-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20191223_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktime',
            name='hours_worked',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]