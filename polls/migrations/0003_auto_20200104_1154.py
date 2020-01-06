# Generated by Django 3.0 on 2020-01-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200104_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workplace',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'New'), (2, 'Approved'), (3, 'Cancelled'), (4, 'Finished')]),
        ),
    ]