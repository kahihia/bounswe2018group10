# Generated by Django 2.1.2 on 2018-10-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]