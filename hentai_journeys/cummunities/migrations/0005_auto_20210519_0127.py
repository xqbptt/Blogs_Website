# Generated by Django 3.1.4 on 2021-05-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cummunities', '0004_auto_20210519_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='Add post', null=True),
        ),
    ]