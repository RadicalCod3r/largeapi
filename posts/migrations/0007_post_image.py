# Generated by Django 4.1.3 on 2022-11-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/users/user.jpg', upload_to='images/posts/'),
        ),
    ]
