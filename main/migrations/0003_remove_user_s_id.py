# Generated by Django 4.2.7 on 2023-11-09 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_s_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='s_id',
        ),
    ]
