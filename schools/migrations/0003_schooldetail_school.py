# Generated by Django 3.2.5 on 2021-07-31 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_schoolsimportfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooldetail',
            name='school',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schools.school'),
            preserve_default=False,
        ),
    ]
