# Generated by Django 4.2.4 on 2023-08-11 14:45

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='نام')),
                ('body', models.TextField(verbose_name='متن کامنت')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('active', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.productmodel')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
                'ordering': ['created'],
                'indexes': [models.Index(fields=['created'], name='products_co_created_791b2f_idx')],
            },
        ),
    ]