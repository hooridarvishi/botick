# Generated by Django 4.2.1 on 2023-09-01 05:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_commentmodel_created_alter_imagemodel_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
