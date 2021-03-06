# Generated by Django 3.2.5 on 2021-08-20 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_alter_schoolreviews_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='school_logo',
        ),
        migrations.AddField(
            model_name='school',
            name='school_image',
            field=models.CharField(default='', max_length=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='sf_ratio',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='board',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='school',
            name='co_ed_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='school',
            name='ownership',
            field=models.CharField(max_length=50),
        ),
    ]
