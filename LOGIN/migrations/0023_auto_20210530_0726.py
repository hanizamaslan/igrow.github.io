# Generated by Django 3.1.2 on 2021-05-29 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0022_auto_20210530_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='Email',
            new_name='SEmail',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='Password',
            new_name='SPassword',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='Username',
            new_name='SUsername',
        ),
    ]
