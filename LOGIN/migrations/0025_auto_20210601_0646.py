# Generated by Django 3.1.2 on 2021-05-31 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0024_auto_20210531_0923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='ProgrammeName',
            new_name='BProgrammeName',
        ),
    ]
