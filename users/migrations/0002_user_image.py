# Generated by Django 4.1.3 on 2022-11-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='images/users/user.jpg', upload_to='images/users/'),
        ),
    ]
