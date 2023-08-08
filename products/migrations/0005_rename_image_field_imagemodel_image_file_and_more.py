# Generated by Django 4.2.4 on 2023-08-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_imagemodel_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemodel',
            old_name='image_field',
            new_name='image_file',
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='عنوان'),
        ),
    ]
