# Generated by Django 3.2.5 on 2021-08-14 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_is_staff_user_is_stafff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_stafff',
        ),
    ]
