# Generated by Django 3.0 on 2019-12-23 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_manager_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='time_limit',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_worked', models.IntegerField()),
                ('record_date', models.DateTimeField(auto_now_add=True)),
                ('workplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.WorkPlace')),
            ],
        ),
    ]