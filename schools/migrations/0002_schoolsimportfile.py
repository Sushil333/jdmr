# Generated by Django 3.2.5 on 2021-07-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolsImportFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schools_import', models.FileField(upload_to='temp')),
            ],
        ),
    ]
