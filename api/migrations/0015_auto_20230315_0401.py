# Generated by Django 3.1.7 on 2023-03-15 04:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20230315_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='last_called',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
