# Generated by Django 3.1.7 on 2023-03-15 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20230315_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='last_called',
            field=models.DateTimeField(default='2023-03-13 23:47:21.145667', null=True),
        ),
    ]
