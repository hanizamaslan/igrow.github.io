# Generated by Django 3.1.2 on 2021-02-18 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0002_auto_20210117_1725'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Person',
        ),
    ]
