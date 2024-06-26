# Generated by Django 3.1.7 on 2023-03-13 23:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20230313_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='device_info',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='ip',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='match_pref',
            field=models.CharField(default='Any', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='open_or_close',
            field=models.CharField(default='Open', max_length=255),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='player_name',
            field=models.CharField(default='SnowNullFix', max_length=125),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='player_numb',
            field=models.CharField(default='Any', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='player_pref',
            field=models.CharField(default='Any', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='team_league',
            field=models.CharField(default='SL', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='team_name',
            field=models.CharField(default='SnowNullFix', max_length=125),
            preserve_default=False,
        ),
    ]
