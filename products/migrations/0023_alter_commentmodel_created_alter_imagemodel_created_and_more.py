# Generated by Django 4.2.1 on 2023-09-01 05:35

from django.db import migrations
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_commentmodel_created_alter_imagemodel_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='publish',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='updated',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
    ]
