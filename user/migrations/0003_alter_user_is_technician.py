# Generated by Django 4.2.1 on 2023-06-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20230602_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_technician',
            field=models.BooleanField(default=False, verbose_name='Is technician'),
        ),
    ]
