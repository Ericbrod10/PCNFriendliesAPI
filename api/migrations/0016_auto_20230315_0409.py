# Generated by Django 3.1.7 on 2023-03-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20230315_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='last_called',
            field=models.DateTimeField(null=True),
        ),
    ]