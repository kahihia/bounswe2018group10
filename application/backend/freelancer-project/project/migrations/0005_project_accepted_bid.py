# Generated by Django 2.1.2 on 2018-11-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_milestone_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='accepted_bid',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
