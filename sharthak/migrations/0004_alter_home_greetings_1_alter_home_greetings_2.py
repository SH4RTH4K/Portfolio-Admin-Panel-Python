# Generated by Django 5.2.4 on 2025-07-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharthak', '0003_alter_home_greetings_1_alter_home_greetings_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_2',
            field=models.CharField(max_length=20),
        ),
    ]
