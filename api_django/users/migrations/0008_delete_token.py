# Generated by Django 4.2.3 on 2023-07-17 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Token',
        ),
    ]
