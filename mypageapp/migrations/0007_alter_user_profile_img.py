# Generated by Django 3.2.5 on 2022-01-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypageapp', '0006_alter_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.FileField(blank=True, null=True, upload_to='MEDIA_URL'),
        ),
    ]
