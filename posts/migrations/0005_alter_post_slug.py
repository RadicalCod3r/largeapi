# Generated by Django 4.1.3 on 2022-11-04 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
