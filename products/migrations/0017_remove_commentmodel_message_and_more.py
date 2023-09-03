# Generated by Django 4.2.1 on 2023-08-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_commentmodel_created_alter_imagemodel_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='message',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='message_negative_points',
            field=models.TextField(default='', max_length=250, verbose_name=' نکات منفی'),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='message_positive_points',
            field=models.TextField(default='', max_length=250, verbose_name=' نکات مثبت'),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='message_text',
            field=models.TextField(default='', max_length=250, verbose_name=' متن پیام '),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='title',
            field=models.CharField(default='', max_length=250, verbose_name='عنوان نظر'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='email',
            field=models.EmailField(default='', max_length=250, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='phone',
            field=models.TextField(default='', max_length=250, verbose_name=' تلفن'),
        ),
    ]
