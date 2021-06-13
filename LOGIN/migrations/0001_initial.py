# Generated by Django 3.1.2 on 2021-01-08 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(upload_to='images/')),
                ('video', models.FileField(upload_to='uploads/')),
                ('graph', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=150)),
                ('Password', models.CharField(max_length=150)),
                ('Username', models.CharField(max_length=150)),
                ('Name', models.CharField(max_length=150)),
                ('DateOfBirth', models.CharField(max_length=150)),
                ('Age', models.IntegerField()),
                ('District', models.CharField(max_length=150)),
                ('State', models.CharField(max_length=150)),
                ('Occupation', models.CharField(max_length=150)),
                ('About', models.CharField(max_length=150)),
                ('Gender', models.CharField(max_length=1)),
                ('MaritalStatus', models.CharField(max_length=150)),
            ],
        ),
    ]
