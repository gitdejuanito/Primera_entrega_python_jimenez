# Generated by Django 4.1.5 on 2023-01-10 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinero',
            name='existe',
            field=models.BooleanField(default=True),
        ),
    ]
