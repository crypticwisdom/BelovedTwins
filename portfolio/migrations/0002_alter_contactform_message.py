# Generated by Django 3.2.5 on 2021-07-14 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]