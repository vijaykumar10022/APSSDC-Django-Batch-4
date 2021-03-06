# Generated by Django 3.0.8 on 2020-08-18 01:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('CSE', 'cse'), ('ECE', 'ece'), ('EEE', 'eee'), ('CIVIL', 'civil'), ('MEC', 'mec')], max_length=20)),
                ('subject', models.CharField(choices=[('DJANGO', 'django'), ('PYTHON', 'Python'), ('C-Lang', 'c-lang'), ('java', 'java')], max_length=50)),
                ('material', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(max_length=500)),
                ('uploadingdate', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
