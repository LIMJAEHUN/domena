# Generated by Django 3.2.3 on 2021-06-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210603_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rogophoto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='회사사진'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=10, null=True, verbose_name='작성'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='등록시'),
        ),
    ]
