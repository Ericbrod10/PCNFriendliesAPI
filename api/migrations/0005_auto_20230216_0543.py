# Generated by Django 3.1.7 on 2023-02-16 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20230216_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
