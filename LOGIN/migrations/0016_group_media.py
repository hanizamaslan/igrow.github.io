# Generated by Django 3.1.2 on 2021-04-09 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0015_auto_20210401_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='Media',
            field=models.FileField(default='', upload_to='uploads/'),
        ),
    ]
